<?php

include 'lib/utils.php';
include 'lib/login.php';

session_start();

if (isset($_POST['user']) && isset($_POST['pass'])) {
    $id = LoginDB::login($_POST['user'], $_POST['pass'], 'press');

    if ( $id ) {

        $_SESSION['id'] = $id;
        
        setcookie("session", base64_encode( json_encode(array("id" => $id, "type" => "press")) ), time() + 10000, "/");

        redirect('press.php');

    } else {
        sleep(1);
        redirect('media.html?fail');
    }
}

redirect('index.html');

?>