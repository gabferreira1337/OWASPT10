# Vulnerable Password Reset
***
#### Even with brute-force protections , such as rate limiting and CAPTCHAs, it's possible to abuse of business logic bugs to take over other user's accounts.

### Guessable Password Reset Questions
#### Web applications commonly use question-based passwords by requesting users to answer some security questions (one or multiple) . The weakest point of most question-based password reset functionalities, is the predictability of the answers.
##### Example of common security questions:
* "What is your mother's maiden name?"
* "What city were you born in?"

#### The answer to these type of questions can often be obtained through `OSINT` or guessed, depending on the number of attempts.

#### To brute-force city related questions we can use this [world-cities.csv](https://github.com/datasets/world-cities/blob/master/data/world-cities.csv) wordlist, for example:
#### Since the CSV file contains the city name in the first field, we can create our wordlist containing only the city name on each line using the following command
```bash
$ cat world-cities.csv | cut -d ',' -f1 > city_wordlist.txt
```

#### Then we simply use `ffuf` to execute our brute-force attack with the above wordlist:
```bash
$  ffuf -w ./city_wordlist.txt -u http://pr1337.org/security_question.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -b "PHPSESSID=34g75j001i3rhy4top1plhb7bn" -d "security_response=FUZZ" -fr "Incorrect response."
```

#### Depending on the information gatered about our target, we could filter the cities to decrease the time required for the brute-force attack.
#### For example, if we knew which country is our target from, we could create a wordlist containing only cities from that contry:
```bash
$ cat world-cities.csv | grep Italy | cut -d ',' -f1 > italian_cities.txt
```


### Manipulating the Reset Request
#### By manipulating a potentially hidden parameter to reset the password of a different account , we can exploit a vulnerable password reset logic.

#### To mitigate this vulnerability, it's crucial to maintain a consistent state throughout the password reset process. Since resetting an account's password is highly sensitive, even small implementation errors or logic flaws could allow attackers to compromise user accounts. Therefore, it's important to thoroughly review the password reset feature of any web application and stay alert to potential security risks.