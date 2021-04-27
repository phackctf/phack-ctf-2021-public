<?php

include 'lib/utils.php';

sessionManagment('search.php');

if (!isset($_GET['name']) || empty($_GET['name'])) {
    die ('ERROR: Missing or empty parameter "name"');
}

sleep(4);

die(
    "This server is running an unsupported MySQL version (Error while connecting to MySQL: Connector::DBI::Mysql connect(...) failed: Can't connect to local MySQL server using file '/var/www/html/old_Test_Database.sql' (2) at /usr/local/mysql/MysqlUtils/Connector.pm line 136.
    Ask your system administrator to upgrade MySQL to improve security and features."
);

?>