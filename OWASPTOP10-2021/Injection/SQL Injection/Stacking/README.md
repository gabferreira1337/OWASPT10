# Stacking SQL Queries
***
#### Stacking SQL queries, also known as **"piggy-backing"** involves injecting extra SQL statements after a vulnerable one. For non-query statements (like INSERT, UPDATE, or DELETE) to run, the platform must support stacking (e.g., Microsoft SQL Server and PostgreSQL do by default). SQLMap can exploit these vulnerabilities to execute non-query statements, enabling advanced features like OS command execution and data retrieval, similar to time-based blind SQL injection.
#### Example
```sql
; DROP TABLE users
```
