# Password Attacks
***
### Basic HTTP AUTH
#### This authentication method uses a user ID and a password for authentication. A user , after sending a request without authentication info, receives a response from the server with the header `WWW-Authenticate`. Then the user is asked to input the authentication information. Consequently, the server transmits a character string that tells the client who is requesting the data. Finally , the client Base64 encode the identifier and  password, and sends that to the server in the Authorization header field. 

### Types of password attacks
* **Dictionary attack**
* **Brute force**
* **Traffic interception**
* **Man In the Middle**
* **Key Logging**
* **Social engineering**


### Brute Force Attack
#### A brute force attack is executed by trying all possible character combinations with a specified length.
#### For instance, if we specify a length of 5 , then the brute force attack will test all keys from `aaaaa` to `zzzzz`.
#### However, a brute force attack is not the best option to perform a password attack, as it would be time-consuming testing all the combinations.

### Dictionary Attack
#### This attack uses a list or lists , instead of brute forcing all combinations.
#### [Password Wordlists](https://github.com/danielmiessler/SecLists/tree/master/Passwords)  and   [Username Wordlists](https://github.com/danielmiessler/SecLists/tree/master/Usernames)

### Methods of Brute Force Attacks
* **Online Brute Force Attack**    -> Attacking a live application over the network, like HTTP, HTTPs, SSH, FTP, and others
* **Offline Brute Force Attack**   -> Also known as Offline Password Cracking, where you attempt to crack a hash of an encrypted password.
* **Reverse Brute Force Attack**   -> Also known as username brute-forcing, where you try a single common password with a list of usernames on a certain service.
* **Hybrid Brute Force Attack**    -> Attacking a user by creating a customized password wordlist, built using known intelligence about the user or the service.



