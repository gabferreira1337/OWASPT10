# Evasion Tools
***
### Bashfuscator
### Tool to obfuscate bash commands
#### Setup:
```shell
$ git clone https://github.com/Bashfuscator/Bashfuscator
$ cd Bashfuscator
$ pip3 install setuptools==65
$ python3 setup.py install --user
```

#### Simple examples:
```shell
$ ./bashfuscator -c 'cat /etc/passwd'
```

```shell
$  ./bashfuscator -c 'cat /etc/passwd' -s 1 -t 1 --no-mangling --layers 1
```

#### And then test the output
```shell
$ bash -c 'eval "$(W0=(w \  t e c p s a \/ d);for Ll in 4 7 2 1 8 3 2 4 8 5 7 6 6 0 9;{ printf %s "${W0[$Ll]}";};)"'
```
### Interactive tool to obfuscate OS commands
#### Setup:
```shell
> git clone https://github.com/danielbohannon/Invoke-DOSfuscation.git
> cd Invoke-DOSfuscation
> Import-Module .\Invoke-DOSfuscation.psd1
> Invoke-DOSfuscation
Invoke-DOSfuscation> help
``` 

#### Simple examples:
```shell
Invoke-DOSfuscation> SET COMMAND type C:\Users\student\Desktop\flag.txt
Invoke-DOSfuscation> encoding
Invoke-DOSfuscation\Encoding> 1'
```

#### And then test the output
```shell
yp%TEMP:~-3,-2% %CommonProgramFiles:~17,-11%:\Users\h%TMP:~-13,-12%b-stu%SystemRoot:~-4,-3%ent%TMP:~-19,-18%%ALLUSERSPROFILE:~-4,-3%esktop\flag.%TMP:~-13,-12%xt

test_flag
```


#### **Note** = Through Linux VM it's also possible to run the above tool, using the **pwsh** .