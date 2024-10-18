# PHP Filters
***
#### When we identify an LFI vulnerability we can use different [PHP Wrappers]() to extend our LFI exploitation, and even potentially reach remote code execution.
#### PHP Wrappers are utilized to access I/O streams at the application level, file descriptors, and memory streams. They can also be used to read PHP source code files and execute system commands.

### Input Filters
#### [PHP Filters]( ) are a type of PHP Wrappers, and are used to  filter the input passed to them by a specified filter.
#### In order to use the PHP Wrapper streams we can use the `php://` scheme , and to access the PHP filter wrapper `php://filter/` .
#### There are several parameters that we can use with the filter wrapper, but the most important ones are `resource` and `read`. The `resource` parameter is used to specify the stream we would like to apply the filter on , while the `read`parameter applies different filters on the specified resource.

#### We can utilize the four filters available : [String Filters](), [Conversion Filters](), [Compression Filters](), and [Encryption Filters]().

### Fuzzing For PHP Files
#### Firstly, we should fuzz for different available PHP pages. Even if their HTTP response code does not return 200, we should be able to read their source code as well.

### Standard PHP Inclusion
#### Normally, when including any php file through LFI it will get executed and rendered as an HTML page.
#### For instance, when trying to include the `config.php` page , we may get an empty result in place of the LFI string. This can happen as the `config.php` most likely only sets up the web app configuration, thus not rendering any HTML output.
#### When our main goal is to read the PHP source code through LFI , we can use the `base64` php filter to base64 encode the php file, and get the encoded source code instead of being executed and rendered.
#### This can be useful in cases where we have a LFI with appended PHP extensions , as we are restricted to including PHP files.

### Source Code Disclosure
#### After collecting potential PHP files  that we want to read , we can start exfiltrating their sources with the `base64` PHP filter
```
php://filter/read=convert.base64-encode/resource=config
```