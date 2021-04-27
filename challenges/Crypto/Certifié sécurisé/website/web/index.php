<?php

if (isset($_POST['pseudo']) and isset($_POST['pass'])) {
    if ($_POST['pseudo'] == "admin" and hash('sha256', $_POST['pass']) == "9aa91108495424296ed1f9d48390928c1146709e02956354da0c4d1a6f265807") {
        echo "Login success !";
    } else {
        echo "Login failed..";
    }
}

?>

<html>
    <form method="POST" action="#">
        <input type="text" name="pseudo" />
        <input type="password" name="pass" />
        <input type="submit" value="login" />
    </form>
</html>