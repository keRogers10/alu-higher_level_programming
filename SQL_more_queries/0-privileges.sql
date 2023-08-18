#!/bin/bash

MYSQL_USER="root"
MYSQL_PASSWORD="nellynello@138712"  

# List privileges for user_0d_1
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"
# List privileges for user_0d_2
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_2'@'localhost';"
