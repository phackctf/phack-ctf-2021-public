<?php

include 'lib/utils.php';
include 'lib/login.php';

session_start();

if (isset($_POST['email']) && isset($_POST['pass'])) {
    $id = LoginDB::login($_POST['email'], $_POST['pass'], 'student');

    if ( $id ) {

        $_SESSION['id'] = $id;
        
        setcookie("session", base64_encode( json_encode(array("id" => $id, "type" => "student")) ), time() + 10000, "/");

        redirect('profile.php');

    } else {
        sleep(1);
        redirect('login.html?fail');
    }
}

redirect('index.html');

?>