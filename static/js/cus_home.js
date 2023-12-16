let menu_icon = document.getElementById('menu_icon');
let cus_menu_box = document.getElementById('cus_menu_box');

menu_icon.onclick = () => {
    if (cus_menu_box.style.visibility == "visible") {
        cus_menu_box.style.visibility = "hidden";
    }
    else {
        cus_menu_box.style.visibility = "visible";
    }

}

let menu_profile_btn = document.getElementById('menu_profile_btn');
let img_map = document.getElementById('img_map');
let profile_display_con = document.getElementById('profile_display_con');

menu_profile_btn.onclick = () => {
    cus_menu_box.style.visibility = "hidden";
    img_map.style.visibility = "hidden";
    delete_con.style.visibility = "hidden";
    profile_edit_con.style.visibility = "hidden";
    profile_display_con.style.visibility = "visible";
}

let profile_edit_bttn = document.getElementById('profile_edit_bttn');
let profile_edit_con = document.getElementById('profile_edit_con');

profile_edit_bttn.onclick = () => {
    cus_menu_box.style.visibility = "hidden";
    profile_display_con.style.visibility = "hidden";
    profile_edit_con.style.visibility = "visible";
}


let profile_delete_bttn = document.getElementById('profile_delete_bttn');
let delete_con = document.getElementById('delete_con');

profile_delete_bttn.onclick = () => {
    cus_menu_box.style.visibility = "hidden";
    delete_con.style.visibility = "visible";
}

let delete_no_btn = document.getElementById('delete_no_btn');

delete_no_btn.onclick = () => {
    cus_menu_box.style.visibility = "hidden";
    delete_con.style.visibility = "hidden";
}


let message_box1 = document.getElementById('message_box1');
let message_box_btn1 = document.getElementById('message_box_btn1');

if (message_box1 != null) {
    let message_h4 = document.getElementById('message_h4').innerHTML;

    message_box_btn1.onclick = () => {
        if (message_h4 == 'Update successfull') {
            img_map.style.visibility = "hidden";
            cus_menu_box.style.visibility = "hidden";
            profile_edit_con.style.visibility = "hidden";
            delete_con.style.visibility = "hidden";
            profile_display_con.style.visibility = "visible";
        }
        else if (message_h4 == 'Phone number or Email Id already exists') {
            img_map.style.visibility = "hidden";
            cus_menu_box.style.visibility = "hidden";
            profile_display_con.style.visibility = "hidden";
            delete_con.style.visibility = "hidden";
            profile_edit_con.style.visibility = "visible";
        }
        else if (message_h4 == 'Login to continue') {
            ride_con.style.visibility = "hidden";
            register_con.style.visibility = "hidden";
            login_con.style.visibility = "visible";
        }
        message_box1.style.visibility = "hidden"

    }
}