-- Lists all previlages of users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
mysql -u root -p nellynello@138712  
source 0-privileges.sql
#!/bin/bash

MYSQL_USER="root"  # Change this to your MySQL username
MYSQL_PASSWORD="nellynello@138712"  

# List privileges for user_0d_1
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"

# List privileges for user_0d_2
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_2'@'localhost';"
