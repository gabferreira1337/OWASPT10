# Enumerating Users
***
#### When a web application responds differently to registered/valid and invalid inputs for authentication endpoints, it's possible to use that vulnerability to enumerate users  from the application.
#### A username can be considered confidential when the web application uses it as a primary identifier for users.
#### Being able to enumerate the usernames can be critical , as users tend to use the same username in different services (**FTP, RDP, SSH, etc.**)
#### Is possible to gather usernames by crawling a web application or using public information, such as company profiles on social networks.

#### Example, a web application has a login form and shows different error messages when inputting a right or wrong username, we can use that to fuzz usernames using a wordslist and filter the response by the proper error message.
```shell
$ ffuf -w /opt/useful/SecLists/Usernames/xato-net-10-million-usernames.txt -u http://172.12.123.123/login.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=FUZZ&password=invalid" -fr "Unknown user"
```
#### After identifying a valid username we can then brute force the user's password.

#### **NOTE**: By inputting an invalid username on a WordPress login, WordPress will, by default, show a different error message ,allowing user enumeration. 

### User Enumeration via Side-Channel Attacks
#### Side-channel attacks focus on exploiting indirect information from a web application, rather than the content of its responses. For instance, an attacker might analyze the response time of a web application. If the application performs database lookups only for valid usernames, the response time might vary slightly depending on whether the username exists. By measuring these timing differences, an attacker could potentially identify valid usernames, even if the actual response message remains unchanged.














