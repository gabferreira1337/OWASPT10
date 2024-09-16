# [HTTP Verb Tampering](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering)
***
#### The HTTP protocol relies on various methods (or **verbs**) at the beginning of an HTTP request, with we applications commonly configured to handle specific methods like **GET** and **POST**. These methods trigger different actions on the server. While developers focus primarily on **GET** and **POST**, a client can technically send requests using other HTTP methods to test how the server reacts.
#### When the web application and server are set up to only accept GET and POST, using other methods will likely result in an error page, which is more of a user experience issue than a security risk. However, if the server is not properly configured and allows unhandled HTTP methods (such as **HEAD** or **PUT**), there is a potential vulnerability. This could enable the attackers to exploit the server, access unauthorized functionalities, or bypass certain security mechanisms.

#### HTTP has 9 different verbs that can be accepted as HTTP methods by web servers. 
#### Other than **GET** and **POST**, we can use the following ones:
* **HEAD** = Response only contains the **headers**
* **PUT** =  Writes request payload to the specified location
* **DELETE** = Deletes the resource at the specified location
* **OPTIONS** = View different options accepted by a web server
* **PATCH** = Insert partial modifications to the resource at the specified location

### Insecure Configurations
#### For instance, an sysadmin may use the following configuration to require authentication on a particular web page:
```xml
<Limit GET POST>
    Require valid-user
</Limit>
```
#### Even though the configuration specifies both **GET** and **POST** request for the authentication method, an attacker may still use a different HTTP method to bypass this authentication mechanism altogether. This could lead to an authentication bypass allowing attackers access web pages and domains they should not have access to.

### Insecure Coding
#### HTTP Verb Tampering can also occur when a web developer applies filters to mitigate particular vulnerabilities while not covering all HTTP methods with that filter. 
#### For instance, a web application vulnerable to a SQLi vulnerability, and the developer mitigated the SQL  Injection vulnerability by adding input sanitization filters:
```php
$pattern = "/^[A-Za-z\s]+$/";

if(preg_match($pattern, $_GET["code"])) {
    $query = "Select * from ports where port_code like '%" . $_REQUEST["code"] . "%'";
    ...SNIP...
}
```

#### As we can see the sanitization filter is only tested on the **GET** parameter. When the **GET** request does not contain any non-valid character, the query will be executed. when the query is executed, the $_REQUEST["code"] parameters are being used, which may also contain POST parameters, **leading to an inconsistency in the use of HTTP Verbs**. Consequently, an attacker could use a **POST** request to perform  SQL Injection, leaving the **GET** request empty (which does not include any non-valid character). 