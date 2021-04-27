<!DOCTYPE html>
<html lang="en" >
  <head>
    <meta charset="UTF-8">
    <title>Step 4 - Hello World</title>
    <link rel="stylesheet" href="./static/style.css">
    <link rel="icon" href="./static/favicon.ico" />
  </head>
  <body>
    <div class="container">
      <h1 id="headline">Ce texte n'est pas encodé en base64.</h1>
      <p><?php echo base64_encode("step-5-1c3ef706.php") ?></p>
    </div>
  </body>
</html>
