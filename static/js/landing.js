let login_con = document.getElementById('login_con');
let register_con = document.getElementById('register_con');
let ride_con = document.getElementById('ride_con');
let auth_login = document.getElementById('auth_login');
let auth_register = document.getElementById('auth_register');
let register_login = document.getElementById('register_login');
let login_register = document.getElementById('login_register');


let message_box1 = document.getElementById('message_box1');
let message_box_btn1 = document.getElementById('message_box_btn1');

if (message_box1 != null) {
    let message_h4 = document.getElementById('message_h4').innerHTML;

    message_box_btn1.onclick = () => {
        if (message_h4 == 'Registration successfull') {
            ride_con.style.visibility = "hidden";
            register_con.style.visibility = "hidden";
            login_con.style.visibility = "visible";
        }
        else if (message_h4 == 'Phone number or Email Id already exists') {
            ride_con.style.visibility = "hidden";
            login_con.style.visibility = "hidden";
            register_con.style.visibility = "visible";
        }
        else if (message_h4 == 'Login to continue') {
            ride_con.style.visibility = "hidden";
            register_con.style.visibility = "hidden";
            login_con.style.visibility = "visible";
        }
        message_box1.style.visibility = "hidden"

    }
}

auth_login.onclick = () => {
    ride_con.style.visibility = "hidden";
    register_con.style.visibility = "hidden";
    login_con.style.visibility = "visible";

}

auth_register.onclick = () => {
    ride_con.style.visibility = "hidden";
    login_con.style.visibility = "hidden";
    register_con.style.visibility = "visible";

}

login_register.onclick = () => {
    ride_con.style.visibility = "hidden";
    register_con.style.visibility = "hidden";
    login_con.style.visibility = "visible";

}

register_login.onclick = () => {
    ride_con.style.visibility = "hidden";
    login_con.style.visibility = "hidden";
    register_con.style.visibility = "visible";

}

