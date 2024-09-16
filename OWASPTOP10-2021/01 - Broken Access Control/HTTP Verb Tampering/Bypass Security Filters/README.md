# Bypass Security Filters
***
#### Another common HTTP Verb Tampering vulnerability is caused by **Insecure Coding** error made during the development of the web application, which consequently would lead to web application not covering all HTTP methods in certain functionalities. This is commonly seen in security filters that detect malicious requests.
#### For instance a security filter being used to detect injection vulnerabilities and only checked for injections in **POST** parameters (e.g `$_POST['param']`), it may be possible to bypass it by simply changing the request method to **GET**.

