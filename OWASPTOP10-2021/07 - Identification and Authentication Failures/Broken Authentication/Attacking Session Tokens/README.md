# Attacking Session Tokens
***
#### With a valid session token of another user, an attacker could impersonate the user to the web application, thus taking over their session.

### Brute-Force Attack
#### When a session token doesn't provide enough randomness and is cryptographically weak, we could brute-force valid session tokens . This  can happen if a session token is too short or contains static data that does not provide randomness to the token (i.e it provides [insufficient entropy](https://owasp.org/www-community/vulnerabilities/Insufficient_Entropy))
#### Let's consider the following scenario, where the token consists of hardcoded prepended and appended values with a small part of the session token being dynamic to provide randomness.
```txt
2c0c58b27c71a2ec5bf2b4b6e892b9f9
2c0c58b27c71a2ec5bf2b4546092b9f9
2c0c58b27c71a2ec5bf2b497f592b9f9
2c0c58b27c71a2ec5bf2b48bcf92b9f9
2c0c58b27c71a2ec5bf2b4735e92b9f9
```
#### After sending some requests we can check that 28 of 32 characters are static (`2c0c58b27c71a2ec5bf2b4`+ 4 characters + `92b9f9`), so we can try and enumerate the other 4 characters to brute-force all existing active sessions, enabling us to hijack all active sessions

#### Another example would be an incrementing session identifier:
```
141233
141234
141237
141238
141240
```
#### The enumeration of all past an future sessions would be easy as we only need to increment or decrement our session token to obtain active sessions and hijack other user's accounts.

### Attacking Predictable Session Tokens
#### More commonly, the session token does provide sufficient randomness on the surface. However, it still can be predicted by an attacker with knowledge of session token generation logic.
#### Example of a predictable session token containing encoded data:
```bash
$ echo -n dXNlcj0xMzM3O3JvbGU9dXNlcg== | base64 -d

user=1337;role=user
```
#### When there's no measure in place preventing us from tampering with the data, we could forge our own session token by manipulating the data and base64-encoding it to match the expected format. <this enables us to forge an admin cookie:
```bash
$ echo -n 'user=1337;role=admin' | base64

dXNlcj0xMzM3O3JvbGU9YWRtaW4=
```

#### We could abuse the same exploit for cokkies containing differently encoded data. For instance, a session token containing hex-encoded data:
```bash
$ echo -n 'user=htb-stdnt;role=admin' | xxd -p

757365723d313333373b726f6c653d61646d696e
```


#### ***NOTE***: It's crucial to capture multiple session tokens and analyze them to ensure that session tokens provide enough randomness to disallow brute-force attacks against them.

