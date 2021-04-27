<?php define('PASS', 'dragon'); ?>

<!DOCTYPE html>
<html lang="en" >
  <head>
    <meta charset="UTF-8">
    <title>Etape 5 - Hello World</title>
    <link rel="stylesheet" href="./static/style.css">
    <link rel="icon" href="./static/favicon.ico" />
  </head>

  <body>
    <div class="container">
      <h1 id="headline">Ne crack pas ce hash MD5, et ne soumet pas le résultat via le formulaire.</h1>
      <p><?php echo md5( PASS ) ?></p>
      <form method="POST">
          <input type="text" name="clear"/>
          <input type="submit" value="Envoyer" />
      </form>
      <?php
        if (isset($_POST['clear']) && md5($_POST['clear']) === md5( PASS ) ) {
            echo '<a href="step-6-c1867dd2.php">Etape 6</a>';
        }
      ?>
    </div>
  </body>
</html>
