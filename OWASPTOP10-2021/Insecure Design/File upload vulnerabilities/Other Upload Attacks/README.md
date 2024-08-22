# Other Upload Attacks
***
### Injection in File Name
#### A common attack vector in file uploads involves using a malicious string as the file name. If the web application displays or processes this file name, it can trigger unintended actions. For instance, if the file name is included in an OS command by the application, it could result in command injection.
#### For example, naming a file file$(whoami).jpg, file\whoami`.jpg, or file.jpg||whoamicould lead to command injection if the web application uses the file name in an OS command likemv file /tmp. The embedded whoami` command would be executed, potentially allowing remote code execution. You can refer to the Command Injections module for more details.
#### Similarly, an XSS payload in the file name, such as `<script>alert(window.origin);</script>`, could execute on a user's machine if the file name is reflected on the page. Additionally, an SQL injection could be attempted by naming the file something like file';select+sleep(5);--.jpg, which might trigger SQL injection if the file name is improperly used in a query.

### Upload Directory Disclosure
#### In some file upload forms, such as feedback or submission forms, we might not have direct access to the link of our uploaded file or know the location of the uploads directory. In these situations, fuzzing can be used to discover the uploads directory. Additionally, other vulnerabilities like LFI (Local File Inclusion) or XXE (XML External Entity) attacks can help locate uploaded files by allowing us to read the web application's source code, as discussed earlier. The Web Attacks/IDOR module also covers various techniques for finding where files are stored and identifying the naming conventions used.
#### Another approach to revealing the uploads directory involves triggering error messages, as they often contain valuable information for further exploitation. For instance, uploading a file with a name that already exists or sending two identical upload requests simultaneously might cause the server to display an error message indicating it couldn't write the file, potentially exposing the uploads directory. Similarly, uploading a file with an excessively long name (e.g., 5,000 characters) might cause an error if the application doesn't handle it properly, which could also reveal the upload path.
#### We can also try other methods to force the server to generate errors that might disclose the uploads directory and other useful details.

### Windows-specific Attacks
#### In some attacks, we can leverage Windows-specific techniques for greater impact.
#### One such technique involves using reserved characters like |, <, >, *, or ?, which are typically reserved for special functions like wildcards. If the web application doesn't properly sanitize these characters or wrap file names in quotes, they could mistakenly refer to another file or trigger an error that reveals the uploads directory. Similarly, using reserved Windows names such as CON, COM1, LPT1, or NUL for a file name can also cause errors, as Windows won't allow files with these names.
#### Another approach is exploiting the Windows 8.3 filename convention, where older versions of Windows shortened file names using a tilde (~). For example, a file named hackthebox.txt might be referenced as HAC~1.TXT or HAC~2.TXT. Since Windows still supports this convention, an attacker could write a file like WEB~.CONF to overwrite an important file like web.conf. This could lead to information disclosure, denial of service (DoS), or even unauthorized access to sensitive files.

### Advanced File Upload Attacks
#### There are more advanced techniques that can exploit file upload functionalities. If a web application automatically processes uploaded files, such as by encoding a video, compressing a file, or renaming it, these processes can be vulnerable if not securely implemented.
#### Some widely used libraries might have known exploits for such vulnerabilities. For example, the AVI upload vulnerability in ffmpeg can lead to an XXE attack. However, when custom code or libraries are involved, identifying these vulnerabilities requires more sophisticated knowledge and techniques. This expertise can potentially uncover advanced file upload vulnerabilities in certain web applications.



