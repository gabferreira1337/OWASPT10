# Insecure Direct Object Reference (IDOR)
***
### Insecure Direct Object References (IDORs) are a type of security flaw that arises when an application allows users to directly access internal objects or resources, such as private files and resources  by manipulating input parameters.
### This vulnerability occurs when proper access controls are not implemented, enabling attackers to modify input values to gain unauthorized access to sensitive data or functionalities.

### IDOR Information Disclosure Vulnerabilities
#### This type of vulnerabilities happen when we can access private files and resources of other users that should not be accessible to us, like personal files or credit card data.
### IDOR Vertical/Horizontal Privilege Escalation
#### With IDOR vulnerabilities we may exploit them to elevate our privileges , for example from a user to an administrator. For instance,some web application expose URL parameters or APIs for admin-only functions in the front-end code and disable them for non-admin users. However, if we had access to those parameters or APIs, we could call them with our user privileges. With a vulnerable implementation on the backend (ex. doesn't explicitly deny non-admin users from calling these functions), it would be possible to perform unauthorized administrative operations, such as changing users' passwords or granting users certain roles that could lead to a complete takeover of the web application.  
**Note**: IDOR vulnerabilities where notably highlighted in the OWASP 2007 top ten list. They represent just one instance of numerous implementations errors that can lead to circumvention of access controls and compromise system security.