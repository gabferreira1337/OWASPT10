# OR injection
***
#### To bypass authentication using SQLi, the goal is to craft a query that will always evaluate to 'TRUE', regardless of the username and password entered.
#### This can be achieved by leveraging the 'OR' operator in SQL, which return 'TRUE' if at least one of its conditions it's true.
#### Given the SQL operator precedence, the 'AND' operator is evaluated before the 'OR' operator. This means that if you can introduce an 'OR' condition that always returns 'TRUE', the entire query will evaluate as 'TRUE'
#### For example:
* `admin' OR '1' = '1`
* The final query should be as follows: `SELECT * FROM users WHERE username='admin' OR '1' = '1' AND password = 'root';`
#### The 'AND' operator will be evaluated first, and it will return false. Then , the OR operator would be evaluated, and if either of the statements is true, it would return true.

#### When we don't know the username we can use the following payloads to log in
* In the username input field: admin`'OR 1=1'`
* In the password input field: 1337`'OR 1=1'`
* The final query should be as follows: `SELECT * FROM users WHERE username='admin' OR 1=1 AND password = '1337' OR 1=1;`
