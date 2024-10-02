# SQL injection in different contexts
***
#### It's also possible to perform SQLi attacks using various input formats like for example, **JSON** or **XML** that the application processes as SQL queries. Some websites accept data in these formats to interact with their database.
#### Exploiting these alternative formats can provide ways to obfuscate attacks, especially when facing defenses like Web Application Firewalls (WAFs). Many security mechanisms scan for common SQL injection keywords, and attackers may attempt to bypass these filters by encoding or escapping characters in restricted keywords.
* For instance, the provided XML-based SQLi example showcases the injection of a malicious SQL query within an XML input:
``` 
<checkStock>
    <productId>1337</productId>
    <storeId>420 &#x53;ELECT TABLE_NAME FROM information_schema.tables</storeId>
</checkStock>
```