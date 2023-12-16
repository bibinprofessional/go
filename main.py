from flask import Flask, request, redirect,url_for, session, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app=Flask(__name__)

app.secret_key = 'secret_key'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Extention@1'
app.config['MYSQL_DB']='go'

mysql=MySQL(app)

pickup=''
drop=''

@app.route('/',methods=['GET','POST'])
def landing():
    message=''
    if request.method=='POST':
        if 'email_login' in request.form and 'user_driver' not in request.form:
            email_login=request.form['email_login']
            password_login=request.form['password_login']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('Select * from user where email = %s and password =%s',(email_login,password_login))
            user=cursor.fetchone()
            if user:
                session['loggedin']=True
                session['id']=user['id']
                session['name']=user['name']
                return redirect('/ride')
            else:
                message='Invalid credentials'
                return render_template('landing.html',message=message)

        elif 'email_login' in request.form and 'user_driver' in request.form:
            email_login=request.form['email_login']
            password_login=request.form['password_login']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('Select * from driver where email = %s and password =%s',(email_login,password_login))
            user=cursor.fetchone()
            if user:
                session['loggedin']=True
                session['id']=user['id']
                session['name']=user['name']
                return redirect('/drive')
            else:
                message='Invalid credentials'
                return render_template('landing.html',message=message)


        elif 'email' in request.form:
            name=request.form['name']
            dob=request.form['dob']
            phone=request.form['phone']
            email=request.form['email']
            password=request.form['password']
            user_check=request.form['user_check']

            if user_check=="1":

                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('Select * from user where phone = %s or email =%s',(phone,email))
                user=cursor.fetchone()

                if user:
                    message='Phone number or Email Id already exists'
                    return render_template('landing.html',message=message,user=user)
                else:

                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('insert into user (name,dob,phone,email,password) values (%s,%s,%s,%s,%s)',(name,dob,phone,email,password))
                    mysql.connection.commit()

                    message='Registration successfull'
                    return render_template('landing.html',message=message)
            
            else:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('Select * from driver where phone = %s or email =%s',(phone,email))
                user=cursor.fetchone()

                if user:
                    message='Phone number or Email Id already exists'
                    return render_template('landing.html',message=message)
                else:

                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('insert into driver (name,dob,phone,email,password) values (%s,%s,%s,%s,%s)',(name,dob,phone,email,password))
                    mysql.connection.commit()

                    message='Registration successfull'
                    return render_template('landing.html',message=message)


        else:
            global pickup,drop
            pickup=request.form['pickup']
            drop=request.form['drop']
            message='Login to continue'
            return render_template('landing.html',message=message)
            

    return render_template('landing.html')

@app.route('/ride',methods=['GET','POST'])
def cus_home():
    message=''
    id=session['id']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('Select * from user where id =%s',(id,))
    user=cursor.fetchone()
    if request.method=='POST':
        if 'name' in request.form:
            name=request.form['name']
            dob=request.form['dob']
            phone=request.form['phone']
            email=request.form['email']
            password=request.form['password']

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('Select * from user where id !=%s and (phone=%s or email=%s)',(id,phone,email))
            user1=cursor.fetchone()
            if user1:
                message='Phone number or Email Id already exists'
                return render_template('cus_home.html',message=message,user=user)
            
            else:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('update user set name=%s,dob=%s,phone=%s,email=%s,password=%s where id=%s',(name,dob,phone,email,password,id))
                mysql.connection.commit()

                cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor2.execute('Select * from user where id =%s',(id,))
                user=cursor2.fetchone()
                message='Update successfull'
                return render_template('cus_home.html',message=message,user=user)
        elif len(request.form)==0:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('delete from user where id=%s',(id,))
            mysql.connection.commit()
            session.pop("id",None)
            session.pop("name",None)
            session['loggedin']=False
            return redirect('/')
            

    
    
    return render_template('cus_home.html',pickup=pickup,drop=drop,user=user)

@app.route('/ride_logout/<int:id>',methods=['GET'])
def cus_logout(id):
    session.pop("id",None)
    session.pop("name",None)
    session['loggedin']=False
    return redirect('/')


@app.route('/drive',methods=['GET','POST'])
def driver_home():
    return render_template('re.html',message='dsfds')


if __name__=="__main__":
    app.run(host='0.0.0.0',port='85',debug=True)
