# Blind OS command injection
***
### In scenarios where an application is vulnerable to blind OS command injection, meaning it doesn't reveal the output of the executed command in its HTTP responses, alternative techniques are employed for detection and exploitation.

## Executing time delays
***
### A good example involves a website that allows users to submit a form, with the server-side application generating an email to a site admin, using an OS command. In this context, the output of the command is not directly visible in the application's responses, necessitating different approaches.
### One technique for detecting blind OS command injection involves leveraging time delays.
### Instead of relying on the typical echo payload to confirm execution, a command is injected to induce a time delay, and the confirmation is based on the duration it takes for the application to respond.
* Example:
  * ```& ping -c 10 127.0.0.1 &```
* The ping command is often used for time delays, since it allows the specification of ICMP packets to send, effectively controlling the runtime of the injected command. 

## Exploiting by redirecting output
***
### Another alternative strategy involves redirecting the command output into a file within the web root. By doing that it's possible to access the command's output from a web browser.
* For instance, consider a situation where the application serves images resources from the filesystem location **/var/www/images**. In this case, it's possible to submit the following input:
  * `& whoami > /var/www/images/whoami.txt &`
* In this command, the **'>'** directs the output of the **'whoami'** command to the specified file(`/var/www/images/whoami.txt`).
* By accessing the following URL **'https://1337example.com/whoami.txt'** it's possible to retrieve the file and visualise the correspondent output from the injected command.