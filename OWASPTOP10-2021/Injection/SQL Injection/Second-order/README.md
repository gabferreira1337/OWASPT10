# Second-order SQL injection
***
#### **First-order** SQL injection happens when an application immediately incorporates user input from an HTTP request into a SQL query without proper safeguards. The input is used in a way that exposes vulnerabilities and allows potential malicious manipulation of the database.
#### On the other hand, **second-order** SQLi occurs when the application takes user input from an HTTP request, stores it for future use (usually in a db), and then, at a later time when handling a different HTTP request, retrieves the stored data. The stored data is then integrated into a SQL query without adequate precautions, leading to a security vulnerability. 
#### This delayed incorporation of user input into a SQL query is why it's also called a stored SQLi.
