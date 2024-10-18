# [Local File Inclusion (LFI)](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion)
***
### Basic LFI
#### For instance, a web application that allows users to change their language, by modifying the URL lang parameter (e.g. `http://<IP>:<PORT>/index.php?lang=pt.php`). If the web application is pulling a file that is now being included in the page, we may be able to change the file being pulled to read the content of a different local file. We can check that by trying to read the `/etc/passwd` file on Linux servers or the `C:\Windows\boot.ini` file on Windows servers changing the lang param:
```
http://<IP>:<PORT>/index.php?lang=/etc/passwd
```

### Path Traversal
#### In the example above , we specified the absolute path of a file (e.g `/etc/passwd`), but this would only work if the whole input was used within the `include()`function without any additions:
```php
include($_GET['language']);
```
#### However, in most occasions web developers append or prepend a string to the respective parameter. For instance, it could be used for the filename, and then added after a directory:
```php
include("./languages/" . $_GET['lang']);
```
#### If we had tried to insert the /etc/passwd path into the parameter with the include function above, the path would have been ./languages//etc/passwd. Since this file does not exist, we would not have been able to read anything.

#### This restriction can easily be bypassed, by traversing directories using relative paths. In order to do that , we can add `../` before our file name, referring to the parent directory.
```
http://<IP>:<PORT>/index.php?lang=../../../../etc/passwd
```
#### As this technique also works even when the entire parameter is used in the `include()` function, we should default to it. Also , if we are at the root path (`/`) and used `../` then we would still remain in the root path, so if we don't know which directory is the web application in , we may add `../` as many times, without breaking the path.

### Filename Prefix
#### On some occasions , our input may be appended after a different string . For instance, it may be used with a prefix to get the full filename:
```php
include("lang_" . $_GET['lang']);
```

#### In the example above , if we try to traverse the directory with `../../../etc/passwd`, the final string would be `lang_../../../etc/passwd`, which is invalid. So, instead of directly using path traversal, we can prefix a `/` before our payload to consider the prefix as a directory, bypassing the filename.
```
http://<IP>:<PORT>/index.php?lang=/../../../etc/passwd
```
#### As the lang_ directory may not exist it could break our file inclusion technique.

### Appended Extensions
#### There are some cases where an extension is appended to a parameter, so the file extension does not have to be written everytime.
```php
include($_GET['lang'] . ".php");
```
#### If we tried to read `/etc/passwd`, the file included would be `/etc/passwd.php`.

### Second-Order Attacks
#### LFI attacks can manifest in various forms, with a more advanced version being the Second-Order Attack. This occurs when a web application retrieves files from the server based on user-controlled parameters in an insecure way.
#### For example, if an application allows users to download their avatar via a URL like /profile/$username/avatar.png, an attacker might exploit this by injecting a malicious username (e.g., ../../../etc/passwd) to access sensitive local files. The attack works by placing a harmful payload into a database entry, such as a username, which another functionality of the application later uses without proper validation.
#### Developers often miss this type of vulnerability because they focus on securing direct user inputs, like query parameters, but may trust values stored in the database, making second-order attacks possible.

