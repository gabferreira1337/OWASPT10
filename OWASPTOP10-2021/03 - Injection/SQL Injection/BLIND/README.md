# Blind SQLi attacks
***
#### Blind SQL injection ia a type of security vulnerability that occurs when an application is susceptible to SQL injection, but the potential attacker cannot directly observe the results of the injected SQL query in the application's HTTP responses.
## Exploiting blind SQL injection by triggering conditional responses
***
* Example-1: Imagine an application that utilizes tracking cookies (e.g., "TrackId") to collect analytics on user usage. When processing requests, it checks whether the provided "TrackId" corresponds to a known user through a SQL query. 
* Cookie: TrackId=133424fdfRRRtD \
`SELECT TrackId FROM TrackedUsers WHERE TrackId = '133424fdfRRRtD'`
* While the application does not directly return the results of this query, it exhibits distinct behavior based on whether the query finds any data. Due to this behavior, it is possible to exploit the blind SQLi vulnerability by retrieving information through conditionally triggering different responses based on an injected condition.
* Example-2:
1. `'...tD' AND '1'='1'`
2. `'...tD' AND '1'='2'`
* In the first case, the injected condition 'AND '1'='1' is true, causing the SQL query to return results.
* In the second case, the injected condition 'AND '1'='2' is false, leading the SQL query to not return the same results.
* This behaviour allows the attacker to determine the truth or falsity of a single injected condition by observing the application's response. By systematically injecting different conditions and observing the corresponding responses, an attacker can extract data one piece at a time.
* For example: Determining the password for a user (e.g., Admin) character by character.
* `...tD' AND SUBSTRING((SELECT Password FROM USER WHERE Username = 'Admin'), 1, 1) = 'a'`
# Error-based SQLi
***
#### When exploiting blind SQLi, some applications may not visibly respond to changes in boolean conditions in the injected SQL queries. In such cases, a different approach is needed. By manipulating the query to intentionally cause a SQL error under certain conditions, we can observe variations in the application's response. This occurs because an unhandled error triggered by the database can lead to noticeable differences, such as error messages, in the application's behaviour.
#### An attacker might manipulate an application to elicit an error message revealing data returned by a query , effectively transforming a blind SQLi vulnerability into an classic SQLi.
#### The attacker may employ the ***CAST()*** function, allowing the conversion of one data type to another.  
* Consider a scenario where a query incorporates the following statement:
* `CAST((SELECT username FROM users) AS int)`
* Typically, the type of data that the attacker want to retrieve is in string format. Attempting to convert it to an incompatible data type, such as an integer, could provoke an error resembling the following:
* `ERROR: invalid input syntax for type integer: "user1337"`
# Exploiting blind SQL injection by triggering time delays
***
#### In scenarios where an application adeptly manages and gracefully handles database errors during SQL query execution, the conventional technique of inducing conditional errors for exploitation becomes ineffective. In such cases, where the application's response remains consistent despite errors, an alternative approach is to exploit blind SQLi vulnerabilities by introducing tmie delays contingent on the truth or falsity of an injected condition.
#### Given the typical synchronous processing of SQL queries by applications, delaying the execution of a SQL query consequently prolongs the time it takes to receive the HTTP response. By strategically orchestrating time delays, an attacker can discern the veracity of the injected condition based on the duration of the HTTP response.
##### Exploiting blind SQLi through time delays involves manipulating SQL queries to introduce delays, with the specific method depending on the database type. For instance, consider PostgresSQL, where it's possible to employ the following techniques to test conditions and induce delays:
* `'; IF (1=3) pg_sleep(10)'--`
* `'; IF (1=1) pg_sleep(10)'--`
* In the first example, the condition `1=3` is false, so no delay is triggered.
* In the second example, the condition `1=1` is true, causing a delay for 10 seconds.
* To retrieve data one character at a time, a technique involves structuring a query like this:
* `'|| (SELECT CASE WHEN (username = 'administrator' AND SUBSTRING(password, 1, 1) = 'a' THEN pg_sleep(10) ELSE pg_sleep(-1) END FROM users)--`
* This query tests whether the substring of the password, starting with the first character, is equal to 'a'. If true, it introduces a time delay. The process is repeated for each character, allowing the gradual retrieving of the password.
* **NOTE**: Diverse database systems may necessitate distinct approaches to implement time delays within SQL queries.


