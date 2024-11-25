# Session Hijacking
***
#### Session Hijacking happens when we take session identifiers from a target and use them to authenticate to the server.
#### It is possible to get a target's session token by following the below methods:
* Passive Traffic Sniffing
* Cross-Site Scripting (XSS)
* Browser history or log-diving
* Read access to a database containing session information

### Simple Example:
#### First we identify the session identifier
#### Then we choose one of the options above to try to get the identifier of our target
#### Finally, we would insert into our browser to get access to the user's data



