# Bypassing Filters
***

### Client-Side Validation
#### In order to bypass these protections, we can either ***modify the upload request to the back-end server***, or we can ***change the front-end code to disable these type validations***.

### Back-end Request Modification
#### Using burp to intercept the request, we can change the **filename** and **file content** in order to input our web shell.
#### We can also change the content type , but at this point it's not needed


### Disabling Front-End Validation
#### By inspecting with the **Page Inspector** , we can find which function is doing the verification and then erase it .
```html
<input type="file" name="uploadFile" id="uploadFile" onchange="checkFile(this)" accept=".jpg,.jpeg,.png">

```

```html
<input type="file" name="uploadFile" id="uploadFile" onchange="" accept=".jpg,.jpeg,.png,.php">
```

#### **Note**: Some browsers may have different methods to change the source code, like the use of **overrides** in Chrome.


### Blacklist Filters
#### There are mostly 2 forms of validating a file extension on the  back-end
1. testing against a **Blacklist** of types
2. testing against a **Whitelist** of types

#### These validation methods may also check for the file content and/or type. Being the weakest one , the blacklist.
#### For instance
```php
$fileName = basename($_FILES["uploadFile"]["name"]);
$extension = pathinfo($fileName, PATHINFO_EXTENSION);
$blacklist = array('php', 'php7', 'phps');

if (in_array($extension, $blacklist)) {
    echo "File type not allowed";
    die();
}
```

#### This small piece of code is taking the file extension and then comparing it against a list of blacklisted extensions. However, this is a weak validation , as other extensions are not included in that list.
#### Also, the extension comparison above  is case-sensitive. In Windows servers, file names are case-insensitive, so we can try and upload a php script with a mixed-case **(.pHP)**.

### Fuzzing Extensions
#### To be able to bypass the file extension verification we can try and fuzz the upload functionality with a list of potential extensions, and check which extension can be used to input our shell.
#### List of extensions for fuzzing [PHP applications](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/Extension%20PHP/extensions.lst) and [.NET applications](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/Extension%20ASP)
#### [SecLists Web Extensions](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-extensions.txt)
#### We may use Burp Intruder functionality or other fuzzing tools (like FFUF)

### Non-Blacklisted Extensions
#### Then after retrieving all non-blacklists extensions from the fuzzing tests, we should be able to upload a php file using other extensions, for example.

### Whitelist Filters
#### A whitelist is generally more secure than a blacklist , because it specifies which extension is supported, consequently the list would not be extensive to cover uncommon extensions.
#### Example of a file extensions whitelist test:
```php
$fileName = basename($_FILES["uploadFile"]["name"]);

if (!preg_match('^.*\.(jpg|jpeg|png|gif)', $fileName)) {
    echo "Only images are allowed";
    die();
}
```
#### As we can see the script uses **regex** to test whether the filename contains any whitelist image extensions. Adding a vulnerability, by only checking if contains and not if actually **ends** with it.

### **Double Extensions**
##### In order to bypass the above whitelisting we can use double extensions.
##### For instance if the .png extension was allowed, we could simply add it in our file name and still finish our filename with **.php** (ex. `shell.png.php`):

#### Despite that, it may not always work, as some webapps may use a refined regex pattern.
#### Example:
```php
if (!preg_match('/^.*\.(jpg|jpeg|png|gif)$/', $fileName)) { ...SNIP... }
```

##### The (`^^*\.`) part match everything up to the last (.), then it uses (`$`) at the end to only match extensions that end the filename

### Reverse Double Extensions
#### There are cases where the file upload functionality itself may not be vulnerable, but the web server configuration may lead to a vulnerability
#### For instance, the /etc/apache2/mods-enabled-php7.4.conf for the ***Apache2*** web server may include the following configuration:
```xml
<FilesMatch ".+\.ph(ar|p|tml)">
    SetHandler application/x-httpd-php
</FilesMatch>
```
#### The web server uses a whitelist with a regex pattern that matches `.phar, .php and .phtml`. Yet, this regex pattern can have the same mistake by not ending with `$`. Consequently , any file that contains the above extensions will be allowed PHP code execution, even if it does not end with the PHP extension.
#### For example , the file name (`shell.php.jpg`) should pass the whitelist test as it ends with .jpg, and it would be able to execute PHP code, as it contains **.php** in its name, due to the above misconfiguration.
### Character Injection
#### Another method used to bypass a whitelist validation test is through **Character Injection**. Injecting some characters before or after the fina extension to cause the web application to misinterpret the filename and execute the uploaded file as a PHP script
#### Characters that we can use:
* %20
* %0a
* %00
* %0d0a
* /
* .\
* .
* …
* :
#### For example, `shell.php%00.jpg` works with PHP servers with version 5.X or earlier, as it causes the PHP web server to end the file name after the %00, and save it as shell.php, while passing the whitelist. For web applications hosted on a Windows server we can use a colon `:` before the allowed file extension (e.g. `shell.aspx:.jpg`), which should also write the file as (`shell.aspx`)
#### Bash script to generate all permutations of a file name, where the above characters would be injected before and after both the **PHP** and **JPG** extensions:
```bash
for char in '%20' '%0a' '%00' '%0d0a' '/' '.\\' '.' '…' ':'; do
    for ext in '.php' '.phps'; do
        echo "shell$char$ext.jpg" >> wordlist.txt
        echo "shell$ext$char.jpg" >> wordlist.txt
        echo "shell.jpg$char$ext" >> wordlist.txt
        echo "shell.jpg$ext$char" >> wordlist.txt
    done
done
```


