# Cross-Site Request Forgery (CSRF or XSRF)
***

#### Cross-Site Request Forgery (CSRF or XSRF) is a type of attack where an unsuspecting user is tricked into performing unintended actions on a web application where they are logged in. The attacker typically uses maliciously crafted web pages or links that the victim interacts with to exploit the lack of proper anti-CSRF protections. These malicious actions are executed using the victim's credentials and privileges, allowing the attacker to carry out unauthorized operations as if they were the victim.
#### CSRF attacks often focus on actions that alter the server's state, such as changing account details or making transactions, though they can also aim to access sensitive information. If a regular user is targeted, the attack can result in data theft or unauthorized actions. However, if the victim is an administrator, the attack could compromise the entire web application.
#### One critical aspect of CSRF attacks is that the attacker doesn't need to see the server's response to succeed. As a result, the Same-Origin Policy, which restricts cross-origin data access, does not provide protection against these attacks.

#### To check if a web application is vulnerable to CSRF attacks we should check if:
* All the parameters required for the targeted request can be determined or guessed
* The application's session management is based on HTTP cookies

#### Additionally, to exploit a CSRF vulnerability we need:
* A malicious web page that will issue a valid (croo-site) request impersonating our target
* Our target to be logged into the application at the time when the malicious cross-site request is issued

### Example:
#### 1. Create and serve the below HTML pge
```html
<html>
  <body>
    <form id="submit" action="http://[REAL_WEBSITE]/api/update-profile" method="POST">
      <input type="hidden" name="email" value="hackedby0xlightningg1337@fbi.gov" />
      <input type="hidden" name="country" value="CSRF_POC" />
      <input type="submit" value="Submit request" />
    </form>
    <script>
      document.getElementById("submit").submit()
    </script>
  </body>
</html>
```

```bash
$ python -m http.server 1337
```


