# Further Session Attacks
***
### [Session Fixation](https://owasp.org/www-community/attacks/Session_fixation)
#### Session Fixation happens when an attacker obtains a target's valid session. A vulnerable web application does not assingn a new session token after a successfull authentication. Consequently , an attacker can persuade  the victim into using a session token chosen by the attacker, session fixation enables  an attacker to steal the victim's session and access their account.
#### For example, assuming a web application vulnerable to session fixation uses a session token in the HTTP cookie **session**.
#### Furthermore, the web application sets the user's session cookie to a value provided in the sid GET parameter. With this implementation, a session fixation attack could look like this:
1. An attacker obtains a valid session token by authenticating to the web application. For instance, let us assume the session token is a1b2c3d4e5f6. Afterward, the attacker invalidates their session by logging out.
2. The attacker tricks the victim to use the known session token by sending the following link: http://example.org/?sid=n6b2p3o8k5j8. When the user clicks this link, the web application sets the session cookie to the provided value, 
```http request
 HTTP/1.1 200 OK
[...]
Set-Cookie: session=n6b2p3o8k5j8
[...]
```
3. The victim authenticates to the vulnerable web application. The victim's browser already stores the attacker-provided session cookie, so it is sent along with the login request. The victim uses the attacker-provided session token since the web application does not assign a new one.
4. Since the attacker knows the victim's session token a1b2c3d4e5f6, they can hijack the victim's session.

#### ***NOTE***: Web applications must assign a new randomly generated session token after successful authentication to prevent session fixation attacks.

### Improper Session Timeout
#### Finally, web applications must define a proper [Session Timeout](https://owasp.org/www-community/Session_Timeout) for a session token. After that time defined in teh session timeout has passed, the session will expire, and the session token is no longer accepted. When a web application doesn't define a session timeout, the session token would be valid infinitely, enabling attackers to use a hijacked session effectively forever.
#### For web application security, it's important to configure session timeouts properly. Since every application has unique business needs, there's no one-size-fits-all session timeout. For example, a web app handling sensitive health information should have a session timeout lasting just a few minutes, while a social media platform might opt for a timeout of several hours.