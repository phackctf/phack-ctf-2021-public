<?php
   ob_start();
   session_start();
?>

<html lang = "fr">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Agenda 2</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="css/main.css" />
    <link rel="icon" href="images/favicon.ico" />

    <style>
      h2{
         text-align: center;
         color: black;
         font-size: 3.5rem;
         margin-top: 50px;
      }
    </style>
   </head>

   <body>
      <h2>Dashboard</h2>
      <div class = "container form-signin">

         <?php
            $msg = '';

            if (isset($_SESSION['username'])) {

              echo '<a href="/logout.php"><button type="button" class="btn btn-primary" id="logout">Se déconnecter</button></a></br></br>';

              $image = <<< 'EOF'

                  ░░░░░░░░░░░░░░░░░░░░░░█████████</br>
                  ░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███</br>
                  ░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███</br>
                  ░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██</br>
                  ░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███</br>
                  ░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██</br>
                  ░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██</br>
                  ░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██</br>
                  ░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██</br>
                  ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██</br>
                  █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██</br>
                  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██</br>
                  ░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██</br>
                  ░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█</br>
                  ░░████████████░░░█████████████████</br>

                  </br>
                  </br>
                  BRAVO ! Le flag est PHACK{th3_bUg_H4s_mut4t3d}</br></br>
                  EOF;


                  echo "<div class='flag'>$image</div>";

              }
              else {
                header('Location: /login.php');
                exit;
              }
         ?>
      </div>
   </body>
</html>
