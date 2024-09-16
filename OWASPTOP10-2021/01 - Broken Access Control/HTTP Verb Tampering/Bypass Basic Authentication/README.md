# Bypass Basic Authentication
***
#### In order to exploit HTTP Verb Tampering vulnerabilities, we need to test alternated HTTP methods to see how they are handled by the web server and the web application. 
#### While there are many automated vulnerability scanning tools to identify those types of vulnerabilities ,they usually miss identifying HTTP Tampering vulnerabilities caused by insecure coding, because it needs active testing to see whether we can bypass the security filters in place.

### Identify
***
#### For instance, a web application (File Manager) that allows us to store some files. also there is an option that let us delete a file , but it appears to be restricted to a normal user as it´s not implemented properly.
#### First we need to identify which pages are restricted by this authentication. 
#### Then to exploit those pages , we need to identify the HTTP request method used by the web application. Furthermore, if it uses a **GET** request, we can send a POST request and see whether the web page allows **POST** requests.
#### By detecting that the web server configurations cover both **GET** and **POST** requests, we can try other type, like **HEAD** as it is similar to a **GET** request but does not return the body in the HTTP request. With that, the delete function of the web application may still get executed, when not receiving any output.

#### To check which HTTP methods the server accepts , we can send an **OPTIONS** request:
```shell
$ curl -i -X OPTIONS http://SERVER_IP:PORT/
```