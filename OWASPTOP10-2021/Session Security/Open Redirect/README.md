# Open Redirect
***
#### An Open Redirect vulnerability occurs when an attacker exploits a legitimate website’s redirection feature to send victims to a malicious site. This happens when the application does not properly validate or restrict the URLs it allows for redirection. The attacker simply embeds a link to their malicious website within the redirection parameter of the trusted website and shares this link with the victim.
#### Because the URL appears to originate from a trusted source, victims are more likely to click it, unknowingly being redirected to a site under the attacker’s control. This type of vulnerability is especially valuable to attackers during the initial stages of an attack, as it helps them lure users to phishing pages or other malicious content while leveraging the credibility of the legitimate site.


### Example of vulnerable code:
```php
$vulnerable = $_GET['url'];
header("Location: " . $vulnerable);
```
#### The url would be : vulnerable.org/index.php?url=https://rogue.com

### Common URL parameters:
* ?url=
* ?link=
* ?redirect=
* ?redirecturl=
* ?redirect_uri=
* ?return=
* ?return_to=
* ?returnurl=
* ?go=
* ?goto=
* ?exit=
* ?exitpage=
* ?fromurl=
* ?fromuri=
* ?redirect_to=
* ?next=
* ?newurl=
* ?redir=
