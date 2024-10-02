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
#### Some applications have defenses in place, like blocking specific hostnames or URLs. However, an attacker can still find ways to bypass these defenses
1. **Alternative IP Representation**: Instead of using the blocked hostname like **"127.0.0.1"**, an attacker might use different representations like **"2130706433"** or **"017700000001"**.
2. **Registering Spoofed Domains**: Attackers can register their own domain (e.g "spoofed.burpcollaborator.net") that resolves to the forbidden IP address (**127.0.0.1**).
3. **Obfuscation**: Strings can be obfuscated using techniques like URL encoding or changing the case of characters, making it harder for filters to detect and block malicious input.
4. **Redirect** : Attackers may provide a URL they control, which redirects to the target URL. By using various redirect codes and different protocols (e.g., switching from **"http"** to **"https:"**), they can trick anti-SSRF filters.
***
### SSRF with whitelist-based input filters
#### In situations where applications employ whitelist-based input filters, it's essential to recognize potential vulnerabilities that may arise from oversight in URL parsing mechanisms. Exploiting inconsistencies in the parsing process can enable the circumvention of restrictive input filters.
* Various techniques can be employed:
1. **Credential Embedding**: By incorporating credentials within the URL before the hostname using the **"@"** char, a seemingly valid URL can be constructed, such as: `https://curr-host:1234@1337-host`. This manipulation may deceive the filtering system into allowing unauthorized access.
2. **URL Fragment Manipulation**: Utilizing the **"#"** char to introduce a URL fragment can create a deceptive appearance.
   * For instance, `https://1337-host#curr-host` may mislead the filter by diverting attention to an innocuous portion of the URL.
3. **DNS Hierarchy Exploitation**: Leveraging the DNS naming hierarchy allows for the insertion of required input into a fully-qualified DNS name controlled by the attacker.
   * An example includes constructing a URL like `https://curr-host.1337-host`, manipulating the DNS structure to potentially bypass filtering mechanisms.
4. **URL-Encoding Confusion**: By strategically URL-encoding characters, it is possible to introduce confusion into the URL-parsing process. This becomes particularly effective when the filtering code treats URL-encoded characters differently from the backend HTTP request code. Additionally, attempting double-encoding can exploit servers that recursively decode input. 
***
### Bypassing SSRF filters via open redirection
#### Exploiting open redirection vulnerabilities can sometimes bypass filter-based security measures in SSRF-protected applications. Suppose a user-submitted URL undergoes strict validation to prevent SSRF abuse. However, the allowed application has an open redirection flaw. By using an API supporting redirections, an attacker could create a URL satisfying the filer, leading to a redirect request to the desired backed.
#### For instance, if the application has an open redirection vulnerability like:
* `/product/nextProd?currProdId=1&path=https://google.com`
* redirecting to https://google.com
#### An attacker could abuse this by crafting an SSRF payload:
`Post /product/stock HTTP/2.0 ` \
` Content-Type:application/x-www-form.urlencoded ` \
`Content-Length: 1337` \
`stockApi=http://webstore.org/product/nextProd?currProdId=1&path=http://192.168.0.12/admin`
* In this case, the application validates the stockAPI URL on an allowed domain, triggering the redirection and making a request to the attacker's chosen internal URL, exploiting the SSRF vulnerability.
***

### Common URL schemes used to exploit SSRF vulnerabilities
* `http://` and `https://`: Retrieves Content via HTTP/S requests. It can be used as a way to bypass WAFs, access restricted endpoints, or access points in the internal network.
* `file://`: Reads a file from the local file system. A hacker may use this in the exploitation of SSRF weaknesses to read local files on the web server (LFI)
* `gopher://`: Protocol used to send arbitrary bytes to the specified address. This can be useful to exploit SSRF vulnerabilities, by sending HTTP POST requests with random payloads or communicating with other services , SMTP servers, databases, etc.


### 3 methods to mitigate the risk of SSRF:
* **Input Validation and sanitation**: Implement strict input validation on user-supplied input, especially for URLs or parameters that could be used in requests (preventing **HPP** (HTTP Parameter Pollution)).
* **Use whitelists**: Maintain a whitelist of allowed URLs or IP addresses that the server is allowed to communicate with. This restricts the scope of potential SSRF attacks.
* **Logging and Monitoring**: Implement thorough logging of server-side requests and monitor for suspicious or unexpected behaviour.