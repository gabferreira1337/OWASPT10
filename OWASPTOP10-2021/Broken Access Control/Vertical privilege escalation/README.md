# Broken Access Control - Vertical Privilege Escalation
***
### Vertical privilege escalation occurs when a user gains unauthorized access to functionality they are not supposed to have access to. This typically happens due to unprotected functionality within an application.
* For example: Sensitive administrative functions may be accessible via specific URLs such as "https://1333-example.com/admin", even though they are intended only for administrative users. It's possible to exploit this vulnerability by directly access these URLs or by brute-force using wordlists.
### In certain cases, applications implement access controls at the platform level by restricting access to specific URLs and HTTP methods based on the user's role.
* For instance, access may be denied to certain URLs for particular user groups, such as managers.
  * `DENY: POST, /admin/deleteUser, managers` 
* However, vulnerabilities can arise if the application framework supports non-standard HTTP headers like **X-Original-URL** or **X-Rewrite-URL**.
* This headers can be exploited to override the original request's URL, bypassing any front-end controls that restrict access based on the URL.
``` 
    POST / HTTP/2
    X-Original-URL: /admin/deleteUser 
    ...
```
### Some applications assign access rights or roles to users upon login, storing this information in a location that users can manipulate, such as a hidden field, cookie, or query string parameter.
### The application then grants access based on the submitted value.
* **Example**:
  * `https://1337-example.org/login/home.jsp?admin=true`
  * `https://1337-example.org/login/home.jsp?userRole=1`
* However, this method is insecure as users can alter these values, potentially accessing functionalities they shouldn't, like administrative features.
