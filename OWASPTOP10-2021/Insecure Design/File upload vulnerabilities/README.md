# File upload vulnerabilities
***
### File upload vulnerabilities arise when a web server permits users to upload files to its filesystem without adequately verifying details such as file names, type, content or size.Inadequate enforcement of these restrictions could lead to a scenario where a seemingly harmless file upload feature can be exploited to upload arbitrary and potentially harmful files, including server-side scripts that allow for remote code execution. In other cases, attackers may exploit the vulnerability by sending subsequent HTTP requests for the uploaded file, often with the intention of triggering its execution by the server.

### Exploiting unrestricted file uploads to deploy a ***web shell***
* The most critical scenario occurs when a website not only allows the upload of server-side scripts but also executes them as code.
* Example: A PHP one-liner that reads arbitrary files from the server's filesystem 
```php
<?php echo file_get_contents('/path/to/target/file');?>
```

### Flawed type validation 
#### One way that websites may attempt to validate file uploads is to check that this input-specific Content-Type header matches an expected **MIME** type. Problems can arise when the value of this header is implicitly trusted by the server and if no further validation is performed to check whether the contents of the file match the supposed MIME type, this defense can easily be bypassed. 

### ***Web shell***
#### A web shell is a malicious script that enables an attacker to execute arbitrary commands on a remote web server simply by sending HTTP requests to the right endpoint.
### Preventing file execution in user-accessible directories
#### Preventing the execution of potentially dangerous files in directories accessible to users os crucial for maintaining the security of a server. While it's ideal to prevent such files from being uploaded in the first place, a secondary measure involves configuring the server to only execute scripts with explicitly **MIME** types. If a script slips through the initial checks, the server typically refrains from executing it and may instead return an error message or serve the file contents as plain text.
#### This behaviour not only helps prevent the execution of malicious scripts but also prevents the creation of web shells. However, it's worth noting that such configurations may vary between directories. Directories where users can upload files often have stricter controls compared to other parts of the filesystem assumed to be inaccessible to end users. Nevertheless, if an attacker finds a way to upload a script to a directory not intended for user-supplied files, the server might inadvertently execute the script.
***
### 3 Best practices to help prevent file upload vulnerabilities:
* Whitelist instead of Blacklist: Instead of prohibiting certain file types, create a whitelist of permitted file extensions.
* Avoid directory traversal: Ensure that filenames do not contain substrings that could be interpreted as directory traversal sequences (e.g., **"../"**) .
* Delayed Permanent Storage: Keep uploaded files in a temporary location until they have been fully validated, so that potentially malicious files are not immediately stored in the server's permanent filesystem, giving the opportunity to thoroughly inspect and validate them.
***
