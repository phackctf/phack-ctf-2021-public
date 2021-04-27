<?php

include 'lib/utils.php';

session_start();
session_unset();
session_destroy();

if (isset($_COOKIE['session'])) {
  unset($_COOKIE['session']); 
  setcookie('session', null, -1, '/'); 
}

redirect('index.html');

?>