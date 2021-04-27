<!DOCTYPE HTML>

<?php

include('data-123456789.php');

$mysqli = new mysqli("tor_db", "jean-michel", "zutquelestmonmotdepasse", "vod");
if ($mysqli->connect_errno) {
    echo "Echec lors de la connexion à MySQL : (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

$val = $mysqli->query('select 1 from `platform` LIMIT 1');

if($val == FALSE)
{
		  $mysqli->query("CREATE TABLE s3cr3t(id INT PRIMARY KEY, flag VARCHAR(50) NOT NULL)");
	    $mysqli->query("INSERT INTO s3cr3t(id, flag) VALUES (1, 'PHACK{D0_U_kn0w_sQLm4p?}')");

	    $mysqli->query("CREATE TABLE platform(id INT PRIMARY KEY, name VARCHAR(50) NOT NULL, description TEXT  NOT NULL)");
	    $mysqli->query("INSERT INTO platform(id, name, description) VALUES (1, 'Netflix', '$netflixDesc')");
	    $mysqli->query("INSERT INTO platform(id, name, description) VALUES (2, 'Disney+', '$disneyDesc')");
	    $mysqli->query("INSERT INTO platform(id, name, description) VALUES (3, 'Amazon Prime', '$primeDesc')");
			$mysqli->query("INSERT INTO platform(id, name, description) VALUES (4, 'Salto', '$saltoDesc')");
			$mysqli->query("INSERT INTO platform(id, name, description) VALUES (5, 'Hulu', '$huluDesc')");
			$mysqli->query("INSERT INTO platform(id, name, description) VALUES (6, 'HBO Max+', '$hboDesc')");
}


echo "<!--
       Helping you n00b
       => SELECT * FROM platform WHERE id = '" . $_GET['id'] . "'
-->

";

$res = $mysqli->query("SELECT * FROM platform WHERE id = '" . $_GET['id'] . "'");

$res->data_seek(0);
$row = $res->fetch_assoc();

if ($row == FALSE) {
	$error = TRUE;
}
else {
	$error = FALSE;
	$id = $row['id'];
	$name = $row['name'];
	$description = $row['description'];

}
?>

<html>
	<head>
		<title>PHack VOD</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
		<link rel="icon" type="image/png" href="images/favicon.png" />
	</head>
	<body class="is-preload">
		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<div class="inner">

							<!-- Logo -->
								<a href="index.php" class="logo">
									<span class="symbol"><img src="images/logo.png" alt="" /></span><span class="title">PHack VOD</span>
								</a>

							<!-- Nav -->
								<nav>
									<ul>
										<li><a href="#menu">Menu</a></li>
									</ul>
								</nav>

						</div>
					</header>

					<!-- Menu -->
						<nav id="menu">
							<h2>Menu</h2>
							<ul>
								<li><a href="index.php">Accueil</a></li>
								<li><a href="index.php">Tous les contenus</a></li>
								<li><a href="index.php">Comment ça marche ?</a></li>
								<li><a href="index.php">Créer un compte</a></li>
								<li><a href="index.php">FAQ</a></li>
							</ul>
						</nav>

				<!-- Main -->
				<?php if ($error) {
					echo "<div class='noresult'>Aucun résultat !</div>";
				}
				else {
					?>

					<div id="main">
						<div class="inner">
							<h1><?php echo "$name"; ?></h1>
							<span class="image main"><img src="images/<?php echo "$id"; ?>.jpg" alt="" /></span>
							<p><?php echo "$description"; ?></p>
						</div>
					</div>

					<?php
					}
					?>

					<!-- Footer -->
						<footer id="footer">
							<div class="inner">
								<section>
									<h2>Restons en contact</h2>
									<form method="post" action="#">
										<div class="fields">
											<div class="field half">
												<input type="text" name="name" id="name" placeholder="Nom*" />
											</div>
											<div class="field half">
												<input type="email" name="email" id="email" placeholder="Email*" />
											</div>
											<div class="field">
												<textarea name="message" id="message" placeholder="Message"></textarea>
											</div>
										</div>
										<ul class="actions">
											<li><input type="submit" value="Envoyer" class="primary" /></li>
										</ul>
									</form>
								</section>
								<section>
									<h2>Réseaux Sociaux</h2>
									<ul class="icons">
										<li><a href="#" class="icon brands style2 fa-twitter"><span class="label">Twitter</span></a></li>
										<li><a href="#" class="icon brands style2 fa-facebook-f"><span class="label">Facebook</span></a></li>
										<li><a href="#" class="icon brands style2 fa-instagram"><span class="label">Instagram</span></a></li>
										<li><a href="#" class="icon brands style2 fa-dribbble"><span class="label">Dribbble</span></a></li>
										<li><a href="#" class="icon brands style2 fa-github"><span class="label">GitHub</span></a></li>
										<li><a href="#" class="icon brands style2 fa-500px"><span class="label">500px</span></a></li>
										<li><a href="#" class="icon solid style2 fa-phone"><span class="label">Phone</span></a></li>
										<li><a href="#" class="icon solid style2 fa-envelope"><span class="label">Email</span></a></li>
									</ul>
								</section>
								<ul class="copyright">
									<li>&copy; P'HackCTF 2021. All rights reserved</li>
								</ul>
							</div>
						</footer>
			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
