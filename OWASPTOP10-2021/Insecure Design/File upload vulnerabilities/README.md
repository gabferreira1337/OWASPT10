# File upload vulnerabilities
***
### File upload vulnerabilities arise when a web server permits users to upload files to its filesystem without adequately verifying details such as file names, type, content or size.Inadequate enforcement of these restrictions could lead to a scenario where a seemingly harmless file upload feature can be exploited to upload arbitrary and potentially harmful files, including server-side scripts that allow for remote code execution. In other cases, attackers may exploit the vulnerability by sending subsequent HTTP requests for the uploaded file, often with the intention of triggering its execution by the server.

### Exploiting unrestricted file uploads to deploy a ***web shell***
* The most critical scenario occurs when a website not only allows the upload of server-side scripts but also executes them as code.
* Example: A PHP one-liner that reads arbitrary files from the server's filesystem
* <?php echo file_get_contents('/path/to/target/file'); ?>
***
### ***Web shell***
#### A web shell is a malicious script that enables an attacker to execute arbitrary commands on a remote web server simply by sending HTTP requests to the right endpoint.  
***
### 3 Best practices to help prevent file upload vulnerabilities:
*
*
*
***
