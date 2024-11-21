# Prevention
### File Inclusion Prevention
#### To prevent any direct user input from reaching file-reading functions, it's essential to be cautious with functions that access files. While the list of such functions is not exhaustive, we should treat any file-accessing function as potentially risky.
#### In cases where altering the application structure is impractical, a workaround is to use a restricted whitelist of permissible user inputs. This whitelist maps each allowed input to a specific file to load and provides a default file for any unmatched inputs. In legacy web applications, we could create a whitelist that encompasses all paths currently referenced by the front end. This whitelist could take various forms: a database table mapping IDs to file paths, a script using pattern matching, or a static JSON map linking names to files.
#### With this approach, user inputs don’t go directly into file-access functions. Instead, the application accesses pre-validated files based on the whitelist, effectively avoiding file inclusion vulnerabilities.


### Preventing Directory Traversal
#### If attackers gain control over directories, they could exploit this to access areas outside the intended scope of the web application, potentially launching further attacks through methods they're more familiar with or using widely applicable attack techniques. Directory traversal vulnerabilities, for example, might allow attackers to:
* Access /etc/passwd, potentially revealing SSH keys or valid usernames, enabling password spray attacks.
* Discover and read files for other services on the server, such as the tomcat-users.xml file for Tomcat, which could expose sensitive data.
* Identify valid PHP session cookies, opening the door to session hijacking.
* View configuration files or source code for the web application, which could reveal weaknesses or sensitive information.
#### To guard against directory traversal, it’s best to rely on built-in methods in your programming language or framework that can securely isolate just the filename. In PHP, for instance, basename() extracts only the filename from a full path, ignoring directory structures. When only a filename is provided, basename() simply returns the filename, and if given a full path, it returns whatever follows the last /, treating it as the filename. However, using this 
#### method restricts access to files in specific directories, so applications requiring directory navigation would be limited.
#### Creating custom functions for this purpose can risk missing obscure edge cases. For instance, in Bash, certain wildcard characters like ? and * can be exploited to mimic directory navigation, allowing paths like cat .?/.*/.?/etc/passwd to read restricted files. This wildcard trick does not work in PHP the same way but shows how inconsistencies between languages could allow attackers to bypass custom directory traversal checks. Therefore, relying on native framework functions can add security because other developers often identify and patch such edge cases before they become exploitable in production applications.

#### We may also sanitize the user input by recursively removing any attempts of traversing directories:
```php
while(substr_count($input, '../', 0)) {
    $input = str_replace('../', '', $input);
};
```
### Web Server Configuration
#### To minimize the potential damage from file inclusion vulnerabilities, several configurations can be implemented. For example, disabling the inclusion of remote files globally can significantly reduce risks. In PHP, this is achieved by setting `allow_url_fopen` and `allow_url_include` to Off, which prevents remote file inclusion.
#### Another effective measure is restricting the web application to its root directory to block access to non-web files. Containerizing the application using `Docker` is a modern approach to enforce this, as it isolates the application within a controlled environment. If Docker isn’t feasible, many languages, including PHP, offer ways to restrict file access to the web directory alone. In PHP, adding open_basedir = /var/www in the php.ini file confines access to the specified directory, preventing unauthorized access to files outside of it. Additionally, disabling certain risky modules, such as Expect or mod_userdir in PHP, helps close off potential exploit paths.
#### With these configurations in place, even if a Local File Inclusion (LFI) vulnerability is present, its ability to affect files outside the web application's folder is significantly restricted, reducing its potential impact.

### Web Application Firewall (WAF)
#### A key approach to strengthening application security is implementing a `Web Application Firewall` (WAF), such as `ModSecurity`. One of the main challenges with WAFs is preventing false positives, which occur when legitimate requests are mistakenly blocked. ModSecurity addresses this by offering a `permissive mode that logs potential threats without blocking them. This allows defenders to fine-tune the rules, ensuring that no genuine requests are accidentally denied.
#### Even if an organization opts not to activate blocking mode, running the WAF in permissive mode can serve as an early alert system, signaling attempted attacks on the application.
#### Ultimately, hardening aims to create a resilient outer layer for the application, so that in the event of an attack, defenders gain valuable time to respond effectively.

