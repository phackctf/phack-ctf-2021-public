#!/bin/bash

docker run --rm --name faceboox-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql

mysql -h localhost -u root -p --protocol=tcp

mysqldump -h localhost -u root -p --protocol=tcp -r old_Test_Database.sql thefaceboox