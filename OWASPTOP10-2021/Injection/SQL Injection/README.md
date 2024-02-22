# SQL Injection (SQLi)
***
### **SQL injection** (**SQLi**) is a cybersecurity thread wherein an attacker manipulates the input fields of a web application to inject malicious SQL code into the database queries. By doing this so, the attacker can gain unauthorized access to sensitive date, modify or delete records, and potentially compromise the entire application or server. 
## Detecting SQL injection vulnerabilities
### To manually detect SQLi vulnerabilities in a web application, a systematic set of tests can be conducted on each entry point:
* Test with a single quote char `(')` to identify potential errors or anomalies in the application's response.
#### **Example** : 
*
### 
1. 
2. 
###
#### 
####
#### 
#### 
#### 

***
### 3 Measures to prevent SQL injections
* **Parameterized Queries**: Utilizing parameterized queries, or prepared statements, is crucial for preventing SQL injection vulnerabilities. By parameterizing user input, the query structure remains intact, and potential malicious input is treated as data rather than executable code.
* **Comprehensive Application of Parameterized Queries**: Parameterized queries should be applied consistently across all instances where untrusted input is involved in SQL queries, such as the **WHERE** clause or values in **INSERT** or **UPDATE** statements. However, caution is advised when dealing with other query components, like table or column names or the **ORDER BY** clause, wich require alternative security measures 
* **Whitelist**: Identifying and approving only certain characters, patterns, or values that are allowed in user inputs. Also Whitelisting may include the use of escape characters or encoding to neutralize any attemp to exploit the input with characters that have special meaning in SQL.
***
## 
