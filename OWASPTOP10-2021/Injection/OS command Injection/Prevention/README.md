# Command Injection Prevention
***
### System commands
#### Allways avoid using functions that execute system commands. For that purpose we can use built-in functions to perform only the needed functionality.
#### For instance, in **PHP** if we want to test if a host is up we can use the **fsockopen** function to perform that test.
#### When there is really a situation that we need to execute a system command , we should always input validate and sanitize to avoid any type of injection.

### Input Validation
#### Whe should always validate and then sanitize user input.
#### Input validation checks if the input has the expected format, and it should be done both on the front-end and on the back-end.
#### Example in PHP where we use the **filter_var**
```php
if (filter_var($_GET['ip'], FILTER_VALIDATE_IP)) {
    // call function
} else {
    // deny request
}
```
#### Example using **regex** with **preg_match** function to validate non-standard formats using JS
```js
if(/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ip)){
    // call function
} else{
    // deny request
}
```
#### In NodeJS there are also libraries to validate various standard formats, like [is-ip](https://www.npmjs.com/package/is-ip).
#### Manuals for Input validation [.NET](https://learn.microsoft.com/en-us/aspnet/web-pages/overview/ui-layouts-and-themes/validating-user-input-in-aspnet-web-pages-sites) and [Java](https://docs.oracle.com/cd/E13226_01/workshop/docs81/doc/en/workshop/guide/netui/guide/conValidatingUserInput.html?skipReload=true)


### Input Sanitization
#### Input Sanitization is the process of removing any non-necessary special characters from the input.
#### To perform input sanitization in **PHP** we can use the **preg_replace** function to remove any special character.
#### Example using regex to only allow alphanumerical characters and (.) character:
```php
$ip = preg_replace('/[^A-Za-z0-9.]/', '', $_GET['ip']);
```
#### The same can be done in JS using the **replace** method
```js
var ip = ip.replace(/[^A-Za-z0-9.]/g, '');
```
#### Or using the **DOMPurify** library on a NodeJS back-end:
```js
import DOMPurify from 'dompurify';
var ip = DOMPurify.sanitize(ip);
```

#### When we want to allow all special characters, we can use t he same **filter_var** function to validate the input and then the **escapeshellcmd** filter to escape any special characters. For **NodeJS**, we cna use the escape(ip) function. Altough escaping special characters is not considered a secure practice, as it can be bypassed through various techniques

### Server Configuration

* Use the web server's built-in **Web Application Firewall** (e.g., in Apache **mod_security**), in addition to an external **WAF** (e.g. Cloudflare, Fortinet, Imperva..)
* **Principle of Least Privilege (PoLP)** : running the server as a low privileged user (e.g. www-data)
* **Prevent functions from being executed by the web server**: Example in PHP : **disable_functions=system**
* **Reject double-encoded** requests and non-ASCII characters in URLs
* **Avoid** the use of sensitive/outdated libraries and modules (e.g. **PHP CGI**)


