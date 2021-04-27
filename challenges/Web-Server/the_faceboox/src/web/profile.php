<?php

include "backend/lib/utils.php";
include "backend/lib/users.php";
include "/chall/vendor/autoload.php";

sessionManagment('profile.php');

try {
    $profile = new User( $_SESSION['id'] );

    $loader = new Twig\Loader\FilesystemLoader('./static/html');

    $twig = new Twig\Environment($loader);

    $template = $twig->load('profile.html');

    echo $template->render(array(
        'profile' => $profile,
    ));

} catch (Exception $e) {
    die ('ERROR: ' . $e->getMessage());
}

?>