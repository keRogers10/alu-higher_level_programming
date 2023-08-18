-- Lists all previlages of users
MYSQL_USER="root"
MYSQL_PASSWORD="nellynello@138712" 
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_2'@'localhost';"
mysql -u root -p nellynello@138712 ; 
source 0-privileges.sql



