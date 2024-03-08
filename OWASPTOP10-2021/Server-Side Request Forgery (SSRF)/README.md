# Server Side Request Forgery (SSRF)
***
### Server-side request forgery is a type of web security vulnerability where an attacker manipulates a server-side application to make unintended requests to different locations.
### In a common SSRF attack, the attacker can instruct the server to connect to internal services usually not accessible to the public.Alternatively, they may force the server to connect to arbitrary external systems.
* Example: In a shopping application that lets the user view the current stock of an item in a particular stock . To provide the stock information, the application must query various back-end REST APIs by passing the URL to the back_end API endpoint via HTTP request in the frontend.
* An attacker can modify the **request** to specify a URL local to the server.
* The server retrieves and provides the content of the ***/admin*** URL when requested by a user. Ordinarily, only authenticated users can access the administrative features at this URL and as a result, if an attacker tries to access ***/admin*** directly, they won't gain any value information.
* However, there's a vulnerability: if the request to ***/admin*** originates from the local machine, the usual access controls are bypassed .The application grants full access to the administrative functionality , because the request it comes from a trusted location.
* POST /product/stock HTTP/2.0 \
Content-Type: application/x-www-form-urlencoded \
Content-Length: 120 \
stockApi=http://localhost/admin
***
### SSRF attacks against other back-end systems
#### In certain scenarios, application servers may communicate with backend systems that aren't directly accessible by end-users. These backend systems often use non-routable IP addresses and shielded by the network topology.However, the security measures for these backend systems may be less robust.
#### It's common for internal backend systems to house sensitive functionalities that could potentially be accessed without proper authentication by anyone with the ability to interact with the systems. This setup poses a risk, as unauthorized users might exploit vulnerabilities in the less secure backend systems to gain access to sensitive functionalities.
***
### How to bypass common SSRF defenses
#### Some applications have defenses in place, like blocking specific hostnames or URLs. However an attacker can still find ways to bypass these defenses
1. **Alternative IP Representation**: Instead of using the blocked hostname like **"127.0.0.1"**, an attacker might use different representations like **"2130706433"** or **"017700000001"**.
2. **Registering Spoofed Domains**: Attackers can register their own domain (e.g "spoofed.burpcollaborator.net") that resolves to the forbidden IP address (**127.0.0.1**).
3. **Obfuscation**: Strings can be obfuscated using techniques like URL encoding or changing the case of characters, making it harder for filters to detect and block malicious input.
4. **Redirect** : Attackers may provide a URL they control, which redirects to the target URL. By using various redirect codes and different protocols (e.g., switching from **"http"** to **"https:"**), they can trick anti-SSRF filters.
***
### SSRF with whitelist-based input filters
#### In situations where applications employ whitelist-based input filters, it's essential to recognize potential vulnerabilities that may arise from oversight in URL parsing mechanisms. Exploiting inconsistencies in the parsing process can enable the circumvention of restrictive input filters.
* Here are several techniques that can be employed:
1. **Credential Embedding**:
2. **URL Fragment Manipulation**:
***
### 3 methods to mitigate the risk of SSRF:
* **Input Validation and sanitation**: Implement strict input validation on user-supplied input, especially for URLs or parameters that could be used in requests (preventing **HPP** (HTTP Parameter Pollution)).
* **Use whitelists**: Maintain a whitelist of allowed URLs or IP addresses that the server is allowed to communicate with. This restricts the scope of potential SSRF attacks.
* **Logging and Monitoring**: Implement thorough logging of server-side requests and monitor for suspicious or unexpected behaviour.