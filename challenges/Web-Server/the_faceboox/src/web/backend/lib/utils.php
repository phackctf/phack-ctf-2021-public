<?php

$whiteList = array(
    "student" => array("profile.php", "user.php", "messages.php", "search.php"),
    "press" => array("press.php"),
);

function sessionManagment($page) {
    global $whiteList;

    session_start();

    if (!isset($_COOKIE['session']) || empty($_COOKIE['session']) || !isset($_SESSION['id'])) {
        redirect('login.html');
    }

    $cookie = base64_decode($_COOKIE['session']);
    $json   = json_decode($cookie, true);

    if (!$cookie || $json == NULL) {
        die ('ERROR: Invalid session cookie');
    }

    if (!array_key_exists('id', $json) || !array_key_exists('type', $json)) {
        die ('ERROR: Missing fields in session cookie');
    }

    if ($json['id'] != $_SESSION['id']) {
        die ('ERROR: Provided cookie id (' . $json['id'] . ') must match session id (' .$_SESSION['id']  . ')');
    }

    if (!array_key_exists($json['type'], $whiteList)) {
        die ('ERROR: Session type must be one of : student, press');
    }

    $_SESSION['type'] = $json['type'];

    if (!in_array($page, $whiteList[ $json['type'] ])) {
        die ('ERROR: Account type "' . $json['type'] . '" are not allowed here. Please refer to whitelist : [' . $whiteList[ $json['type'] ][0] . ', ..]');
    }

}

function redirect($location) {
    header('Location: ../' . $location);
    die();
}

# DEBUGING PURPOSE
function x($var) {
    echo '<pre>' . var_export($var, true) . '</pre>';
    // var_dump(LoginDB::$database);
    die();
}

?>