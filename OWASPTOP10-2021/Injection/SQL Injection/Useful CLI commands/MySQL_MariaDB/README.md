# MySQL and MariaDB Basics
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
### Insert new record to a given table
#### Passwords should be hashed/encrypted before storage
```mysql
mysql> INSERT INTO user VALUES('root', 'root');
```

### Insert multiple records to a given table
```mysql
mysql> INSERT INTO user VALUES('root', 'root'), ('notroot', 'notroot');
```
### Retrieve data 
```mysql
mysql> SELECT password FROM user;
```

### Drop (remove) tables and databases from the server 
#### Favorite SQL statement for junior Devs ;)
```mysql
mysql> DROP TABLE user;
```

### Drop (remove) column
```mysql
mysql> ALTER TABLE user DROP points;
```

### Using ALTER to change the name of any table and any of its fields, or delete or add a new column to an existing table
```mysql
mysql> ALTER TABLE user ADD points INT;
```
### Rename Column
```mysql
mysql> ALTER TABLE user RENAME COLUMN nopoints;
```

### Change a column's data type
```mysql
mysql> ALTER TABLE user MODIFY nopoints VARCHAR(5);
```
### Update specific records within a table

```mysql
mysql> UPDATE user SET password = "rootroot" WHERE id > 1;
```

