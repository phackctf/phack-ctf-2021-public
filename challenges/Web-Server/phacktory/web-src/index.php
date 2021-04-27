<?php

include("config-126546845171616835186.php");

// Easter chocolate creation factory
// WIP : Do not send to production, I think it not safe yet. I should ask to my master
//
//              __)),
//             //_ _)
//             ( "\"
//              \_-/
//          ,---/  '---.
//         /     - -    \
//        /  \_. _|__,/  \
//       /  )\        )\_ \
//      / _/  (   '  ) /  /
//     / |     (_____) | /
//    /,'      /     \/ /,
//  _/(_      (   ._, )-'
// `--,/      |____|__|
//            |    )  |
//            |   /   |
//            |  / \  |
//           / `|  | _)
//           |  |  |  |
//           |  /  \  |
//           | |    \ |
//           | \    | \_
//           /__(    '-._`,

class PHackTory {
    public $type;
    public $quantity;

    public function __construct() {
        if(isset($_POST['type'])) {
            $this -> type = $_POST['type'];
        } else {
            $this -> order = "milky";
        }

        if(isset($_POST['quantity'])) {
            $this -> quantity = $_POST['quantity'];
        } else {
            $this -> quantity = "50";
        }
    }

    public function __wakeup() {
      global $DEBUG;

      $types = ["dark", "white", "milky", "fruity", "95%", "flag"];
      $quantities = [1, 5, 10, 25, 50, 100, "PHACK{}"];

      if (isset($this -> type) && isset($this -> quantity)) {
        if(in_array($this -> type, $types) && in_array($this -> quantity, $quantities)) {
            prepareOrder($this);
            return "Votre commande de " . $this -> quantity . " chocholats ("  . $this -> type .  ") est en préparation.";
        }
        else {
          if ($DEBUG) {
            //Affichage des variables pour deboguer. Enfin..Je crois que c'est ça que ca fait.
            eval($this -> type . ' ' . $this -> quantity);
          }

          return "Il semble y avoir un problème avec votre commande. Merci de contacter quelqu'un d'autre.";
        }
      }
    }

    public function prepareOrder(){
      // ToDo
    }
}

$a = $_GET['what'];
$b = $_POST['is'];
$c = $_POST['cool'];
$d = $_GET['the'];

?>

<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>PHackTory</title>
    <link rel="icon" href="images/favicon.ico" />
  </head>
  <body style="background-image: url('images/background.jpg'); background-size: cover;">

    <div style=" position: absolute;
                 left: 20%;
                 top: 25%;
                 width: 60%;
                 padding: 10px;
                 text-align: center;
                 background-color: white;
                 opacity: 0.7;
                 font-size: 3rem;">
       <h1 style="text-decoration: underline;">PHackTory</h1>
        <p>
          Votre magasin se prépare pour les fêtes. <br/>
          Les commandes ne sont pas encore ouvertes.
        </p>
      </div>

    <?php
      if(isset($a) && isset($b) && isset($c) && isset($d)) {
          if($d == "flag" && $a == "is") {
            if ($b > 1538) {
              $myOrder = unserialize($_GET['please']);
              return "Oui !";
            }
            else {
              return "Peut-être !";
            }
          }
          else {
            return "Certainement pas!";
          }
      }
      else {
        return "Non !";
      }
    ?>
  </body>
</html>
