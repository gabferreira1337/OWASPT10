# Comments
***
### In SQLi attacks we can use comments to ignore a certain part of the query
#### In MySQL, we can use 2 types, **--** and **#**, in addition to an in-line comment /**/
#### Example:
* username = admin'-- password = 1337
##### Executing query :
```sql
SELECT * FROM users WHERE username = 'admin'-- 'AND password = 1337;
```
##### As we can see , if we use the -- we can log in as the user admin because we commented out the password part

#### Another Example using parenthesis:
* username = admin')-- password = 1337
```sql
SELECT * FROM users WHERE (username = 'admin')-- ' AND Id > 1) AND password = 1337;
```






### **Note**: In SQL, using 2 dashes only is not enough to start a comment. We need to add an empy space after them, so the comment start with (-- ), with a space at the end. Another important thing to not forget is , when we are inputting a payload in the url within a browser, a (#) symbol is usually considered as a tag, and will not be passed as part of the URL. So in order to use (#) as a comment we can use the URL encoded (#) symbol `%23`