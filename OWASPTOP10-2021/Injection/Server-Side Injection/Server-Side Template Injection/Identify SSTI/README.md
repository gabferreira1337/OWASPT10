# Identifying SSTI
***
#### First we need to identify which template engine is the web application using, in order to prepare our exploitation process accordingly to the syntax of the given engine.

### Confirming SSTI
#### Injecting special characters with semantic meaning in template engines is the best way to  identify an SSTI vulnerability.
#### Test string:
```
${{<%[%'"}}%\.
```
#### After typing the above string , the web application will return any error if it's vulnerable to SSTI.

### Identifying the Template Engine
#### HTB SSTI Template Identification diagram
![htb-SSTI.png](..%2F..%2FImg%2Fhtb-SSTI.png)

#### First we try to input the `${7*7}` payload, then we follow the diagram above, depending on the result of each injection.
#### In ***Jinja***, the result of `{{7*'7'}}` will be 777777, while  in ***Twig***, the result will be 49.

