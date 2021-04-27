<?php

include "backend/lib/utils.php";
include "backend/lib/users.php";
include "/chall/vendor/autoload.php";

sessionManagment('user.php');

if (!isset($_GET['id'])) {
    redirect('user.php?id=1');
}

try {
    
    $profile = new User((int) $_GET['id']);

    $loader = new Twig\Loader\FilesystemLoader('./static/html');

    $twig = new Twig\Environment($loader);

    $template = $twig->load('user.html');

    echo $template->render(array(
        'profile' => $profile,
    ));

} catch (Exception $e) {
    die ('ERROR: ' . $e->getMessage());
}

?>