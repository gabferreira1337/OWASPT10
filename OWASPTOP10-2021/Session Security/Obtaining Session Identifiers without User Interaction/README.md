# Obtaining Session Identifiers without User Interaction
***

### Via Traffic Sniffing
#### Traffic sniffing is a common technique used by penetration testers to assess network security. By connecting their devices (e.g., laptops or Raspberry Pis) to available Ethernet ports, they can monitor network traffic and identify potential attack targets. For this to work, the attacker and victim must be on the same local network, allowing the attacker to inspect protocols like HTTP traffic.
#### In order to obtain session identifiers through traffic sniffing we would need to be positioned on the same local network as the victim and an unencrypted HTTP trafic.

### Session Hijacking via traffic Sniffing

### Obtaining Session Identifiers Post-Exploitation (Web Server Access)
#### We can retrieve session identifiers and data from either a web server's disk or memory.

### PHP
#### The entry `session.save_path` in `PHP.ini` specifies where session data will be stored.

```bash
$ locate php.ini
$ cat /etc/php/7.4/cli/php.ini | grep 'session.save_path'
$ cat /etc/php/7.4/apache2/php.ini | grep 'session.save_path'
```
#### For instance in the default configuration we would see that it would be stored at `/var/lib/php/sessions`

#### Then we would find which sessions are active and the username associated
```bash
$ ls /var/lib/php/sessions
$ cat /var/lib/php/sessions/sess_fsfjaajsdafnasnpsaf
```

### Java
#### "The Manager element represents the session manager that is used to create and maintain HTTP sessions of a web application.
#### Tomcat provides two standard implementations of Manager. The default implementation stores active sessions, while the optional one stores active sessions that have been swapped out (in addition to saving sessions across a server restart) in a storage location that is selected via the use of an appropriate Store nested element. The filename of the default session data file is SESSIONS.ser."


### [.NET](https://www.c-sharpcorner.com/UploadFile/225740/introduction-of-session-in-Asp-Net/)
#### Session data can be found in:
* `aspnet_wp.exe` = Application worker process. InProc Session mode
* `StateServer`  = Windows Service in IIS or separate server. OutProc Session mode
* `An SQL Server`

### Obtaining Session Identifiers Post-Exploitation (Database Access)
#### When we can exploit a SQLi or when we have any database credentials we should check for any stored  user sessions.
```sql
show databases;
use leet;
show tables;
select * from users;
```


