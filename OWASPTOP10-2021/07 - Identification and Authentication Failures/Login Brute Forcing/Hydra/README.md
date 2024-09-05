# [Hydra](https://github.com/vanhauser-thc/thc-hydra)
***
#### Hydra is a reliable tool for Login Brute Forcing. It can fuzz any pair of credentials and perform a fast verification of success. 

### Username Brute Force Example:
```shell
$ hydra -L /opt/useful/SecLists/Usernames/Names/names.txt -p amormio -u -f 171.111.111.111 -s 1337 http-get /
```

### Brute Force Forms
#### To cause minimal network traffic , it is better to try the top 10 most popular admins credentials.
#### If we didn't get any access, we should then use `password spraying`. By reusing passwords .

