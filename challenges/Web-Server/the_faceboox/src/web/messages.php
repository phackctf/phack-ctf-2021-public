<?php

include "backend/lib/utils.php";
include "backend/lib/messages.php";
include "/chall/vendor/autoload.php";

sessionManagment('messages.php');

try {
    
    $messages = MessageDB::get($_SESSION['id']);

    $loader = new Twig\Loader\FilesystemLoader('./static/html');

    $twig = new Twig\Environment($loader);

    $template = $twig->load('messages.html');

    echo $template->render(array(
        'messages' => $messages,
    ));

} catch (Exception $e) {
    die ('ERROR: ' . $e->getMessage());
}

?>