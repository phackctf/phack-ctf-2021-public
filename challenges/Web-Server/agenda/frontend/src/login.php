<?php
   ob_start();
   session_start();
?>

<html lang = "fr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Agenda</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="css/main.css" />
    <link rel="icon" href="images/favicon.ico" />

    <style>
       body {
          padding-top: 40px;
          padding-bottom: 40px;
          background-color: #ADABAB;
       }

       .form-signin {
          max-width: 430px;
          padding: 15px;
          margin: 0 auto;
          color: #017572;
       }

       .form-signin .form-signin-heading,
       .form-signin .checkbox {
          margin-bottom: 10px;
       }

       .form-signin .checkbox {
          font-weight: normal;
       }

       .form-signin .form-control {
          position: relative;
          height: auto;
          -webkit-box-sizing: border-box;
          -moz-box-sizing: border-box;
          box-sizing: border-box;
          padding: 10px;
          font-size: 16px;
       }

       .form-signin .form-control:focus {
          z-index: 2;
       }

       .form-signin input[type="text"] {
          margin-bottom: -1px;
          border-bottom-right-radius: 0;
          border-bottom-left-radius: 0;
          border-color:#017572;
       }

       .form-signin input[type="password"] {
          margin: 10px 0px;
          border-top-left-radius: 0;
          border-top-right-radius: 0;
          border-color:#017572;
       }

       h2{
         text-align: center;
         color: black;
         font-size: 3.5rem;
         margin-top: 50px;
       }

       h4 {
         color: red;
          background-color: white;
          padding: 10px;
          text-align: center;
          opacity: 0.9;
          border-radius: 5px;
       }
    </style>
   </head>

   <body>
      <h2>Connexion</h2>
      <div class = "container form-signin">
         <?php
            $msg = '';
            $msg_display = "none";

            if (isset($_SESSION['username'])) {
              header('Location: /flag.php');
              exit;
            }
            else if (!empty($_POST['username']) && !empty($_POST['password'])) {
               if ($_POST['username'] == 'flagman' && $_POST['password'] == 's3cr3t_d0_n07_Sh4r3') {
                  $_SESSION['valid'] = true;
                  $_SESSION['timeout'] = time();
                  $_SESSION['username'] = 'flagman';

                  header('Location: /flag.php');
                  exit;
               }
               else {
                  $msg = 'Mauvais login et/ou mot de passe';
                  $msg_display = "block";
               }
            }
         ?>
      </div>

      <div class = "container">
         <form class = "form-signin" role = "form" action = "<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>" method = "post">
            <h4 class = "form-signin-heading" style="display:<?php echo $msg_display; ?>"><?php echo $msg; ?></h4>
            <input type = "text" class = "form-control" name = "username" placeholder = "Identifiant" required autofocus />
            <input type = "password" class = "form-control" name = "password" placeholder = "Mot de passe" required />
            <button class = "btn btn-lg btn-primary btn-block" type = "submit" name = "login">Se connecter</button>
         </form>
      </div>
   </body>
</html>
