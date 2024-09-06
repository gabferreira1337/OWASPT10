# [Default Credentials](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials)
***
#### Many web applications come with default login credentials that allow access immediately after installation. However, these credentials must be updated after setup, as leaving them unchanged makes it easy for attackers to gain unauthorized access. Therefore, checking for default credentials is a critical step in authentication testing, as outlined in OWASP's Web Application Security Testing Guide. OWASP notes that common default credentials include combinations like "admin" and "password."
### Testing default credentials
#### There are many platforms who provide lists of default credentials for a variety of web applications. For example:
#### [Web database of Default Credentials](https://www.cirt.net/passwords)
#### We can also search for default credentials on [SecLists Default Credentials](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Default-Credentials) and on the [SCADA GitHub repository](https://github.com/scadastrangelove/SCADAPASS/tree/master)