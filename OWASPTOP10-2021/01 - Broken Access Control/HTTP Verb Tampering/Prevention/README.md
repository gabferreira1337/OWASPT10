# Verb Tampering Prevention
***

### In secure configuration
#### These type of vulnerabilities can occur in most web servers, such as **Apache**, **ASP.NET**, and **Tomcat** , and they usually appear when we limit a page's authorization to a particular set oh HTTP verbs, remaining others unprotected.

### Example of a vulnerable Apache web server configuration, located in the site configuration file (e.g. `000-default.conf`), or in a `.htaccess` web page configuration file:
```xml
<Directory "/var/www/html/admin">
    AuthType Basic
    AuthName "Admin Panel"
    AuthUserFile /etc/apache2/.htpasswd
    <Limit GET>
        Require valid-user
    </Limit>
</Directory>
```

#### The configuration above is setting the authorization configurations for the `admin` web directory. However, by using the `<Limit GET>` keyword , the `Require valid-user`setting will only apply to `GET`requests .Consequently , the page could still be accessible through `POST` requests or other methods , such as `HEAD` or `OPTIONS``

### Example of the same vulnerability on a **Tomcat** web server configuration, which can be found in the web.xml file for some Java web applications:
```xml
<security-constraint>
    <web-resource-collection>
        <url-pattern>/admin/*</url-pattern>
        <http-method>GET</http-method>
    </web-resource-collection>
    <auth-constraint>
        <role-name>admin</role-name>
    </auth-constraint>
</security-constraint>
```

#### The authorization is being limited only to the **GET** request method with `http-method`, thus leaving the page accessible through other HTTP methods.

### Lastly, an example of a vulnerable **ASP.NET** web server configuration, located in the **web.config** file of a web application:
```xml
<system.web>
    <authorization>
        <allow verbs="GET" roles="admin">
            <deny verbs="GET" users="*">
        </deny>
        </allow>
    </authorization>
</system.web>
```
#### As seen on the others, the **allow** and **deny** scope is limited to the **GET** method, which leaves the web application accessible though other HTTP verbs.

#### The examples highlight that restricting authorization to specific HTTP methods is not secure. It's essential to configure the server to allow or deny all methods, not just certain ones. To safely specify methods, use directives like `LimitExcept` in Apache, `http-method-omission` in Tomcat, or `add/remove` in ASP.NET, which exclude only specified methods. Additionally, it's recommended to disable or deny all `HEAD` requests unless explicitly needed by the web application to prevent potential attacks.

### Insecure Coding
#### In order to identify insecure coding , we need to find inconsistencies in the use of HTTP parameters across functions, as in some instances, this may lead to unprotected functionalities and filters.

#### Example of a vulnerable PHP code:
```php
if (isset($_REQUEST['filename'])) {
    if (!preg_match('/[^A-Za-z0-9. _-]/', $_POST['filename'])) {
        system("touch " . $_REQUEST['filename']);
    } else {
        echo "Malicious Request!";
    }
}
```

#### The `preg_match` function it's properly looking for unwanted characters, blocking any data inserted to go into the command if it contains any special character. However, due to the **inconsistent use of HTTP methods** it is possible to perform Command Injection.
#### As we can see, the preg_match filter is only checking for special characters in POST parameters via `$_POST['filename']`. However, the final system command uses `$_REQUEST['filename']`, which handles both GET and POST parameters. This means that when we sent malicious input through a GET request, the preg_match function didn't block it since it only checked POST parameters, which were empty. When the input reached the system function, it used the GET parameters instead, allowing the command injection to occur.

#### **We must be consistent with our use of HTTP methods** and ensure that the same method is always used for any specific over the web application , in order to avoid HTTP Verb Tampering vulnerabilities in our code. We must **expand the scope of testing in security filters** by testing all request parameters with the following functions and variables:

```php
PHP:
$_REQUEST['param']
```

```java
Java:
request.getParameter('param')
```

```
C#:
Request['param']
```