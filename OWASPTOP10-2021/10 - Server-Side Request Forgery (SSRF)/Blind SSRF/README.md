# Blind SSRF
***
#### SSRF Blind vulnerabilities happen when the response it's not demonstrated to us

### Identifying Blind SSRF
#### We can identify Blind SSRF vulnerabilities by inputting a URL to our system and setting up a netcat listener:
```bash
$ nc -lnvp 8000
```

### Exploiting Blind SSRF
#### In order to exploit blind SSRF vulnerabilities we need to see how the web application behaves to various requests. Then we can run a restricted fuzzing, filtering by the different responses that we gathered. 
#### Some web applications send different error messages that can be useful to exploit.
