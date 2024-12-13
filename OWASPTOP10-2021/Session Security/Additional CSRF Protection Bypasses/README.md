# Additional CSRF Protection Bypasses
***
### Null Value
#### When the only check in place is only looking for the header, and it does not validate the token value we may craft our cross-site requests using a null CSRF token.
```
CSRF:
```

### Random CSRF Token
#### Sometimes there are application which only look compares the length of the CSRF to check if it's the same as the original. So we could send a random CSRF token with the same length.

### Use another Session's CSRF token
#### An alternative way to bypass anti-CSRF protections involves using the same CSRF token across different user accounts. This vulnerability exists in applications that do not link the CSRF token to a specific user account and only verify whether the token is syntactically valid.
#### To test for this, create two accounts. Log in to the first account, initiate a request, and capture the CSRF token—for example, `CSRF-Token=a1b2c3d4e5f67890abcd1234ef567890`.
#### Next, log in to the second account and use the same CSRF token (`CSRF-Token=a1b2c3d4e5f67890abcd1234ef567890`) while making a similar or different request. If the application processes the request successfully, it indicates that the same CSRF token is valid across multiple accounts, allowing attackers to exploit this vulnerability and perform CSRF attacks using their own token across other user accounts.



### Request Tampering
#### There are times that when changing the request method the csrf token would not be needed as it could bem an unexpected request
#### Example:
```http request
POST /change_paswd
POST body:
password=root&confirm=root
```

```http request
GET /change_paswd?password=root&confirm=root
```

### Delete the CSRF token parameter or send a blank token

### Session Fixation > CSRF
#### Some web applications use a defense mechanism called a `double-submit cookie` to protect against CSRF. In this approach, a request includes the same randomly generated token both as a `cookie` and as a `request parameter`. The server validates the request by checking if the token in the cookie matches the token in the request. If they are identical, the request is deemed legitimate.
#### However, this approach has a limitation: the application is likely not storing the valid token on the server side. It simply checks for equality between the two tokens without verifying if the token itself is legitimate. This means the server has no way to determine if a received token was actually issued by the application.
#### If the application also has a `session fixation vulnerability`, an attacker could exploit this weakness as follows:
#### Steps:
1. Session Fixation: The attacker forces or sets the victim’s session ID to a known value by exploiting the session fixation vulnerability.
2. CSRF Execution: The attacker crafts a request with a token they generate and ensures it is included both in the cookie and the request parameter. Since the server only checks for equality between the two tokens, it will accept the request as valid, allowing the attacker to perform unauthorized actions.
This bypass demonstrates how a double-submit cookie defense is insufficient if not combined with stronger server-side validation mechanisms.

```http request
POST /change_passwd
Cookie: CSRF-Token=fixed_token;
POST body:
password=root&CSRF-Token=fixed_token
```

### Anti-CSRF Protection via the Referer Header
#### When an application is using  the referrer header as an anti-CSRF mechanism, we may try removing it.
```html
<meta name="referrer" content="no-referrer"
```

### Bypass the Regex


#### In some cases, applications use a regex to validate the Referrer header as part of their CSRF protection, allowing requests only from specific domains. However, poorly designed regex patterns can be exploited to bypass this validation.
#### For instance, if the application checks for google.com in the Referrer header, an attacker might use a crafted URL such as www.google.com.attacker.com or google.com.malicious.site. These URLs include the required substring (google.com) but point to the attacker's domain.
#### Similarly, if the application validates requests from its own domain, such as target.com, you could attempt something like:
* `www.target.com.attacker.site`
* `target.com.malicious.site`
#### Other tricks to test include:
* www.attacker.site?www.target.com
* www.attacker.site/www.target.com
* attacker.site#target.com
#### If the application’s regex is overly permissive or does not strictly validate domain boundaries, these crafted Referrer values may bypass the whitelist and allow unauthorized requests. This demonstrates the importance of implementing strict regex validation or alternative, more secure mechanisms.

