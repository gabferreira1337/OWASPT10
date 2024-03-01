# Blind SQLi attacks
#### Blind SQL injection ia a type of security vulnerability that occurs when an application is susceptible to SQL injection, but the potential attacker cannot directly observe the results of the injected SQL query in the application's HTTP responses.
## Exploiting blind SQL injection by triggering conditional responses
* Example-1: Imagine an application that utilizes tracking cookies (e.g., "TrackId") to collect analytics on user usage. When processing requests, it checks whether the provided "TrackId" corresponds to a known user through a SQL query. 
* Cookie: TrackId=133424fdfRRRtD \
`SELECT TrackId FROM TrackedUsers WHERE TrackId = '133424fdfRRRtD'`
* While the application does not directly return the results of this query, it exhibits distinct behavior based on whether the query finds any data. Due to this behavior, it is possible to exploit the blind SQLi vulnerability by retrieving information through conditionally triggering different responses based on an injected condition.
* Example-2:
1. '...tD' AND '1'='1'
2. '...tD' AND '1'='2'
* In the first case, the injected condition 'AND '1'='1' is true, causing the SQL query to return results.
* In the second case, the injected condition 'AND '1'='2' is false, leading the SQL query to not return the same results.
* This behaviour allows the attacker to determine the truth or falsity of a single injected condition by observing the application's response. By systematically injecting different conditions and observing the corresponding responses, an attacker can extract data one piece at a time.
* For example: Determining the password for a user (e.g., Admin) character by character.
* `...tD' AND SUBSTRING((SELECT Password FROM USER WHERE Username = 'Admin'), 1, 1) = 'a'`
# Error-based SQLi
#### When exploiting blind SQLi, some applications may not visibly respond to changes in boolean conditions in the injected SQL queries. In such cases, a different approach is needed. By manipulating the query to intentionally cause a SQL error under certain conditions, we can observe variations in the application's response. This occurs because an unhandled error triggered by the database can lead to noticeable differences, such as error messages, in the application's behaviour.
* Example: