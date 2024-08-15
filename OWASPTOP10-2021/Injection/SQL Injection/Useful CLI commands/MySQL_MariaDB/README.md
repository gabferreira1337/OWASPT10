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
### UPDATE specific records within a table

```mysql
mysql> UPDATE user SET password = "rootroot" WHERE id > 1;
```

### Query Results

#### Sorting Results
```mysql
mysql> SELECT * FROM user ORDER BY password  DESC;
```
```mysql
mysql> SELECT * FROM user ORDER BY password  DESC, id ASC;
```

#### LIMIT Results
```mysql
mysql> SELECT * FROM user ORDER BY password  DESC, id ASC;
```

#### LIMIT with Offset
```mysql
mysql> SELECT * FROM user LIMIT 1, 2;
```

#### WHERE Clause
```mysql
mysql> SELECT * FROM table_name WHERE  <Condition>;
```

#### LIKE Clause
##### '%' match zero or more chars , '_' match exactly one char
```mysql
mysql> SELECT * FROM user WHERE username  LIKE "admin%";
```
```mysql
mysql> SELECT * FROM user WHERE username  LIKE "___";
```

#### SQL Operators
##### AND
```mysql
mysql> SELECT 1 = 1 AND "test" = "test";
```
##### The result will be true (1)

##### OR
```mysql
mysql> SELECT 1 = 1 OR "test" = "abc";
```
##### The result will be true (1)

##### NOT
```mysql
mysql> SELECT NOT 1 = 2;
```
##### The result will be true (1)

#### Multiple Operator Precedence
* Division (/), Multiplication (*), and Modulus (%)
* Addition (+) and subtraction (-)
* Comparison (=, >, <, <=, >=, !=, LIKE)
* NOT (!)
* AND (&&)
* OR (||)

##### Note: In MySQL/MariaDB we can't add a ';' to execute more queries.