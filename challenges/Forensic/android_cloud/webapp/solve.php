<?php

if ( isset($_GET['debug']) ) {
    echo "Nice try ! :)";
    die();
}

/* REQUEST LIMIT TO BLOCK BRUTEFORCE */

$storing_time = 300; # store tries for 10 minutes
$apc_key = "{$_SERVER['SERVER_NAME']}~login:{$_SERVER['REMOTE_ADDR']}";

apcu_inc($apc_key, 1, $success, $storing_time);  

if (!$success) {
    echo "Fatal error. Contact the CTF admin team.";
    die();
}

$tries = (int) apcu_fetch( $apc_key );

if ($tries > 60) {
    header("HTTP/1.1 429 Too Many Requests");
    echo "You've exceeded the number of unlock attempts. We've blocked IP address {$_SERVER['REMOTE_ADDR']} for 5 minutes.";
    die();
}

$solution = ["1", "5", "2", "4", "8", "7", "6", "9"];
$flag = "PHACK{T4ke_c4rE_oF_Ur_B4cKupS!}";

echo (isset($_POST['path']) && is_array($_POST['path']) && $_POST['path'] === $solution) ? $flag : 'wrong ';