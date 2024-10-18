# Basic Bypasses
***

### Non-recursive Path Traversal Filters
#### Deleting substrings of `../` using a search and replace filter is one of the most basic filters to mitigate LFI:
```php
$lg = str_replace('../', '', $_GET['language']);
```
#### However, the filter above is not recursively removing the `../` substring , thus being insecure. In order to counterattack that filter we can try to use a payload with `....//` , so the filter would only remove `../` and our final string would be `../`
#### Example:
```
http://<IP>:<PORT>/index.php?lang=....//....//....//....//etc/passwd
```
#### We may also try to bypass that filter by using other substrings such as `..././` or `....\|` to escape the forward slash character , and in some cases whe could try to add extra forward slashes `....////`

### Encoding
####  To bypass filters that may prevent  input filters that include certain LFI-related characters, like a `.` or a `/` we may URL encode our input, so it would not contain bad characters , but would still be decoded back to our path traversal string once it reaches a back-end vulnerable function. 
#### Example:
```
http://<IP>:<PORT>/index.php?lang=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%65%74%63%2f%70%61%73%73%77%64
```

### Approved Paths
#### Another method used to mitigate LFI vulnerabilities is by using Regular Expressions ensuring that the file included is under a specific path.
#### For instance, the web application may only accept paths under `./lang` directory.
```php
if(preg_match('/^\.\/languages\/.+$/', $_GET['lang'])) {
    include($_GET['lang']);
} else {
    echo 'Illegal path specified!';
}
```

#### To bypass the above filter we may Fuzz web directories under the same path or examine the requests sent by the existing form to check what path is used .

### Appended Extension
#### Some web applications append an extension to our input string, ensuring that the included file in i n the expected extension. In modern versions of PHP, any tentative to bypass this filter may be blocked, and it will be restricted to only reading files in that extension. Nonetheless, it may still be useful for reading source code, for example.

#### There are some techniques that we can use , but they are eradicated in newer versions of PHP. However, it may still be useful as some web applications may still be using older servers.


### Path Truncation
#### In earlier versions of PHP, there was a limit on string length, where defined strings could not exceed 4096 characters. This restriction likely stemmed from limitations on 32-bit systems. If a string exceeded this length, PHP would automatically cut off the extra characters, ignoring anything beyond the 4096th character. Additionally, PHP used to simplify paths by removing trailing slashes and single dots (for example, calling `/etc/passwd/`. would be treated as `/etc/passwd`). Linux systems, like PHP, also ignore multiple slashes in a path, so a path like `////etc/passwd` is treated the same as `/etc/passwd`. Likewise, the current directory shortcut (`.`) in the middle of a path is disregarded, so `/etc/./passwd` is also treated as `/etc/passwd.
#### By exploiting these behaviors, we could create very long strings that still resolve to valid paths. When a string reaches the 4096-character limit, any extension (like .php) that is appended afterward gets cut off, leaving the path without an extension. For this technique to work, the path must start with a non-existent directory to bypass certain checks.

#### For instance:
```
?lang=leet_directory/../../../etc/passwd/./././././././ [Repeated N times]
```

#### Simple command to generate the above payload: 
```bash
$ echo -n "non_existing_directory/../../../etc/passwd/" && for i in {1..2048}; do echo -n "./"; done
```

### Null Bytes
#### Older versions of PHP were also vulnerable to `null byte injection`, where adding a null byte `%00` at the end of the string would terminate the string and not consider anything after it.
#### For example, we may input the following payload `/etc/passwd%00` that before being passed to the `include()` function it would be `/etc/passwd%00.php` . In the end , everything after the null byte would be truncated, being the final path `/etc/passwd`.
