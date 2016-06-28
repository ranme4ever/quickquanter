DROP DATABASE IF EXISTS db_quickquant;

CREATE DATABASE db_quickquant DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

use db_quickquant;
CREATE TABLE t_user ( id INT(8) NOT NULL PRIMARY KEY auto_increment,
                        username VARCHAR(32) NOT NULL,
                        password VARCHAR(32) NOT NULL,
                        email VARCHAR(64) NOT NULL)DEFAULT CHARSET=utf8;
