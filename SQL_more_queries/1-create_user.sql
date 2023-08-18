<<<<<<< HEAD
-- creates a user and password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@localhost;
FLUSH PRIVILEGES;
=======
-- A script that creates the MYSQL server user.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON . TO 'user_0d_1'@'localhost';
>>>>>>> 60c09660fa7ddf4ac283123721ee801b36978d83
