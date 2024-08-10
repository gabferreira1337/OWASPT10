# MySQL and MariaDB
***

### Connect to a host
```bash
$ mysql -u root -h docker.a133z.us -P 3306 -p
```

#### When host is not specified , it will use the localhost by default

### Creating a Database
```mysql
mysql> CREATE DATABASE users;
```

### Show Databases and Switch to a given Database
```mysql
mysql> SHOW DATABASES;

mysql> USE mysql;
```
### Create a table
```SQL
CREATE TABLE user(
    id SERIAL NOT NULL,   -- id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(80), -- UNIQUE NOT NULL
    password VARCHAR(80),
    date_of_creation DATETIME -- DATETIME DEFAULT NOW()
    PRIMARY KEY (id)
);
```

### Show Tables
```mysql
mysql> SHOW TABLES
```

### List the table structure
```mysql
mysql> DESCRIBE user;
```


