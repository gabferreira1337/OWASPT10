# Limited File Uploads
***

### XSS
####  Through many file types it's possible to exploit a Stored XSS vulnerability, by uploading malicious versions of them.
#### An example is when a web application let us upload HTML files. Consequently , it would be possible to implement JS code in them to carry an XSS or CSRF attack on whoever visits the uploaded HTML page.
#### Other example of XSS attacks is web applications that display an image's metadata after its upload. We can include an XSS payload in one of the Metadata parameters that accept raw text, like the **Comment** or *+Artists** parameters:
```bash
$ exiftool -Comment=' "><img src=1 onerror=alert(window.origin)>' HTB.jpg
$ exiftool HTB.jpg
...SNIP...
Comment                         :  "><img src=1 onerror=alert(window.origin)>
```

#### In some cases we can change the image's MIME-Type to text/html, because some web applications may show it as an HTML document instead of an image, in which case the XSS payload would be triggered even if the metadata wasn't directly displayed.
#### It is also possible to use **SVG** images to carry XSS attacks by modifying their XML data to include an XSS payload
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1" height="1">
    <rect x="1" y="1" width="1" height="1" fill="green" stroke="black" />
    <script type="text/javascript">alert(window.origin);</script>
</svg>
```

### XXE (XML external entity)
#### With SVG images, we can also include malicious XML data to leak the source code of the web application, and other internal documents within the server.
#### Example using a svg image that exfiltrates content of (/etc/passwd).
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<svg>&xxe;</svg>
```
#### Access to the source code will provide ways to find more vulnerabilities to exploit within the web application through **Whitebox Penetration Testing**. Even for file upload exploitation, allowing us to **locate the upload directory, identify allowed extensions, or find the file naming scheme**.
#### Example using XXE to read source code in PHP web apps, we can use the following payload in our SVG image:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg [ <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>
<svg>&xxe;</svg>
```
#### Using XML data isn't exclusive to SVG images; it's also common in various document types, such as PDFs, Word documents, PowerPoint presentations, and others. These documents rely on XML data to define their format and structure. If a web application has a document viewer that is vulnerable to XXE and permits the upload of these document types, an attacker could potentially insert malicious XXE elements into the XML data. This could then be exploited to perform a blind XXE attack on the backend server.

### DoS
#### File upload vulnerabilities can often result in Denial of Service (DoS) attacks on a web server. For instance, the XXE payloads mentioned earlier can be leveraged to execute DoS attacks, as covered in the Web Attacks module.
#### Additionally, a Decompression Bomb can be used with file formats that support data compression, like ZIP files. If a web application automatically extracts uploaded ZIP archives, an attacker could upload a malicious archive containing multiple nested ZIP files. This could expand to several petabytes of data, overwhelming the backend server and causing it to crash.
#### Another potential DoS attack is the Pixel Flood attack, which targets image files that use compression, such as JPG or PNG formats. An attacker could create a JPG image with a normal size (e.g., 500x500 pixels) and then modify its compression data to falsely indicate a much larger size (e.g., 0xffff x 0xffff pixels), resulting in an image perceived as 4 Gigapixels. When the web application tries to render this image, it would attempt to allocate an excessive amount of memory, leading to a server crash.
#### Other methods to trigger a DoS include uploading excessively large files, as some upload forms may not enforce size limits or validate file size before uploading. This could fill the server's storage space, causing it to crash or significantly slow down.
#### If the upload function is vulnerable to directory traversal, an attacker could try uploading files to unintended directories (e.g., ../../../etc/passwd), potentially causing the server to crash. There are various other DoS attacks that can be executed through vulnerable file upload functionalities.





