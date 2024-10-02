# Preventing SSRF
***
#### To mitigate SSRF (Server-Side Request Forgery) vulnerabilities, it's essential to implement countermeasures at both the web application and network layers.
#### At the application level, when fetching data from remote hosts based on user input, enforce security by checking the destination against a whitelist. This prevents attackers from forcing the server to make requests to unauthorized locations, especially internal systems. The URL scheme and protocol should be restricted, either by hardcoding or validating against a whitelist, to prevent the use of arbitrary protocols. Proper input sanitization is also key to avoiding unexpected behaviors that could lead to SSRF.
#### On the network side, firewall rules should be configured to block outgoing requests to unauthorized destinations, effectively stopping potential SSRF attacks. Network segmentation can further protect internal systems by isolating them from external requests, reducing the risk of exploitation through SSRF.


[OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)