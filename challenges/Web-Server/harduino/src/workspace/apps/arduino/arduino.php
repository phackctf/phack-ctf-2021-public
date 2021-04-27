<?php

include "vendor/autoload.php";

try {

    /* Display message */
    $message = "Hello World !";

    /* If custom message is sent, use it instead */
    if (isset($_GET["message"])) {
        $custom = $_GET["message"];
        $message = preg_replace("/^.*$/e", "\"$custom\"", $message);
    }

    /* Twig template loader */
    $loader = new Twig\Loader\FilesystemLoader('./template');
    $twig = new Twig\Environment($loader);
    $template = $twig->load('arduino.html');

    /* Render template */
    echo $template->render(array(
        'message' => $message,
    ));

} catch (Exception $e) {
    die ('ERROR: ' . $e->getMessage());
}

?>