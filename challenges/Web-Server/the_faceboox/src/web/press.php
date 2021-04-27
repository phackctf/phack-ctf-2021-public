<?php

include "backend/lib/utils.php";
include "backend/lib/users.php";
include "/chall/vendor/autoload.php";

sessionManagment('press.php');

try {

    $loader = new Twig\Loader\FilesystemLoader('./static/html');

    $twig = new Twig\Environment($loader);

    $template = $twig->load('press.html');

    echo $template->render(array());

} catch (Exception $e) {
    die ('ERROR: ' . $e->getMessage());
}

?>