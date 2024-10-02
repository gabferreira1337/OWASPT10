# OS Command Injection
***
### OS command injection , also known as ***shell injection*** , is a type of security vulnerability that occurs when an application allows an attacker to inject and execute arbitrary operating system commands on the server. This vulnerability arises when user input is not properly validated or sanitized before being passed to a system command. As a result, an attacker can manipulate iinput fields or parameters to inject malicious commands, leading to the execution of unauthorized actions to the server.
#### Example of a vulnerable PHP and NodeJS code
```php
<?php
if (isset($_GET['filename'])) {
    system("touch /tmp/" . $_GET['filename'] . ".pdf");
}
?>
```
```JS
app.get("/createfile", function(req, res){
    child_process.exec(`touch /tmp/${req.query.filename}.txt`);
})
```
##### As we can see a web application written in PHP  and NodeJS may use functions like, exec, system, shell_exec, passthru,  popen, child_process.exec, or child_process.spawn to execute commands on the server.
* **Example** : An application that provides users with information about the stock status of a particular item. The application achieves this by making a request to a URL, such as:
* `https://1337-example.org/stockStatus?productID=42`
* However, behind the scenes, the application interacts with legacy systems to retrieve this information. The implementation relies on executing a shell command with the product ID as argument:
* `1337Stock.org 42`
* The output of this shell command, which contains the stock status for the specified item, is then returned to the user.
* In this scenario, the application lacks defenses against oS command injection, making it vulnerable to malicious input. An attacker exploits this vulnerability by submitting the following input in the **productID** parameter:
* ` & echo HelloWorld &` and then the resulting command executed by the application becomes:
* `1337Stock.org & echo HelloWorld & `
### **Breaking down the output received by the attacker**:
1. The original `1337stock.org` command is executed without its expected arguments, leading to an error message indicating that **productID** was not provided.
2. The injected `echo` command is successfully executed, echoing the supplied string **"HelloWorld"** in the output.
### Shell metacharacters
#### In OS command injection attacks, various shell metacharacters can be employed to inject malicious commands . These metacharacters serve as command separators, allowing attackers to chain multiple commands together.
#### Command Separators (**Windows and Unix-based systems**)
* `|` , `||` , `&`, `&&`, the OR operator will only execute the second command of the first one fails. The operator '&' puts the first command running in the background
#### Unix-based systems specific command separators:
* `;`, Newline(`0x0a` or `'\n'`)
#### Inline execution on Unix-based systems:
* `(backticks)` , ` injected command \ `, `$(` , `injected command )`
#### Note: In cases where the input under the attacker's control is enclosed within quotation marks in the original command, it becomes necessary to terminate the quoted context (using, `"`, `'`) before injecting new commands with the appropriate shell metacharacters. Also, there is an exception with using the semicolon, which will not work if executed with Windows Command Line (CMD).
***
### Common operators with respective type of Injection
Injection Type | Operators
* **SQL Injection**   ```' , ; -- /* */*```
* **Command Injection**   ```; &&```
* **LDAP Injection**  ```* ( ) & |```
* **XPath Injection**  ```' or and not substring concat count```
* **OS Command Injection**   ```; & |```
* **Code Injection**  ```' ; -- /* */ $() ${} #{} %{} ^```
* **Directory Traversal/File Path Traversal**  ```../ ..\\ %00```
* **Object Injection**  ```; & |```
* **XQuery Injection** ```' ; -- /* */```
* **Shellcode Injection**   ```\x \u %u %n```
* **Header Injection**   ```\n \r\n \t %0d %0a %09```

***
### 3 Best practices to prevent OS command injection attack
* **Avoid shell commands** : Whenever possible, avoid executing shell commands from within your application. Instead, use platform-specific APIs or libraries that provide a safer way to achieve the same functionality
* **Input Validation** : Validate all user inputs thoroughly. Ensure that the inputs conform to expected formats and do not contain any unexpected characters. Use whitelists to permit only known safe values.
* **Regular Security Audits** : Conduct regular security audits of your codebase to identify and address potential vulnerabilities, including any areas where OS command execution is involved.
***
## Some useful commands
* Kill a process - Linux : `kill -9 <pid>`  Windows : `taskkill /F /PID <pid>`
* OS info - Linux : `uname -a`  Windows: `ver`    
* Running processes - Linux : `ps -ef`  Windows: `tasklist`
* Trigger time delay by sending ICMP packets - Linux : `ping -c <num_packets> 127.0.0.1 ` Windows : `ping -n 15 127.0.0.1`
* Network connections - Linux & Windows : `netstat -an`
* Current user - Linux & Windows `whoami`
* Network config - Linux : `ifconfig`  Windows : `ifconfig /all`