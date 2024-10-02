# XSS Prevention
***
#### XSS vulnerabilities typically arise from two critical areas in a web application: the **Source** , such as a user input field, and the **Sink**, where this input is displayed. 
#### To prevent XSS attacks, it's essential to secure both of these aspects, ensuring that user inputs are handled safely both on the client side (front-end) and on the server-side (back-end). This can be achieved by implementing proper sanitization and validation on both ends, and using other security measures.

### Front-end
#### Input validation Example
```javascript
function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test($("#login input[name=email]").val());
}

```

#### Input Sanitization Example Using DOMPurify
```javascript
<script type="text/javascript" src="dist/purify.min.js"/>
let clean = DOMPurify.sanitize(dirty);
```
##### The method sanitize() escapes any special char with a '\\', ensuring that a user does not send anny input with special characters

#### And finally we shouldn't ever use user input directly within certain HTML tags and avoid JS and JQuery functions that allow changing raw text of HTML field:
##### HTML Tags:
1. HTML Comments
2. CSS Style Code <style></style>
3. JS code <script></script>
4. Tag/Attr Fields <div name="INPUT"></div>

##### JS:
1. DOM.innerHTML
2. DOM.outerHTML
3. document.write()
4. document.writeln()
5. document.domain

##### JQuery:
1. html()
2. parseHTML()
3. add()
4. append()
5. prepend()
6. after()
7. insertAfter()
8. before()
9. insertBefore()
10. replaceAll()
11. replaceWith()

#### Back-end
##### On the back-end side to protect against XSS attacks we can implement Input and Output Sanitization and Validation, proper  Server configuration and use back-end tools that help prevent XSS vulnerabilities.

#### Input Validation Example in PHP
```php
if(filter:var($_GET['email'], FILTER_VALIDATE_EMAIL)){
//if validated...
}else{
}
```

#### Input Sanitization in PHP using addslashes function
```php
addslashes($_GET['email'])
```
##### This function sanitizes user input by escaping special characters with a backlash
##### Don't forget that direct user input (e.g. $_GET['email']) should never be directly displayed on the page.

#### Input Sanitization Example in NodeJS using the DOMPurify library (same as in the front-end example)
```JS
import DOMPurify from 'dompurify';
var clean = DOMPurify.sanitize(dirty);
```

#### Output HTML Encoding
##### By encoding any special character into their HTML codes, it can help to display the entire user input without introducing an XSS vulnerability.
##### In PHP whe can use the **htmlspecialchars** or the **htmlentities** functions to encode certain special chars into their HTML codes
##### Example:
```PHP
htmlentities($_GET['username'])
```
##### Example in NodeJS using the html-entities library
```JS
import encode from 'html-entities'
encode('<'); // -> "&lt;"
```
#### Server Configuration
* Using HTTPS across the entire domain.
* Using XSS prevention headers.
* Using the appropriate Content-Type for the page, like X-Content-Type-Options=nosniff.
* Using Content-Security-Policy options, like script-src 'self', which only allows locally hosted scripts.
* Using the HttpOnly and Secure cookie flags to prevent JavaScript from reading cookies and only transport them over HTTPS.

#### Web Application Firewall (WAF)
##### The use of a good WAF can help prevent XSS exploitation, because it will automatically detect any type of injection going through HTTP requests and also automatically reject such requests.
##### Some frameworks also provide built-in XSS protection , like [ASP.NET](https://learn.microsoft.com/en-us/aspnet/core/security/cross-site-scripting?view=aspnetcore-7.0)