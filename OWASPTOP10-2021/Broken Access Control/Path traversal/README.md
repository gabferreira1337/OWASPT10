## Path traversal
***
### Common barriers to leveraging path traversal vulnerabilities

#### Common barriers to leveraging path traversal vulnerabilities are frequently encountered in applications that incorporate user input file paths. Despite the implementation of defenses against path traversal attacks, these barriers can often be circumvented.
#### In instances where an application removes or restricts directory traversal sequences from user provided filenames, alternative techniques may still enable bypassing these defenses.    
* **For example**: Utilizing an absolute path originating from the filesystem root, such as specifying `filename=/etc/passwd`, allows direct referencing of a file without relying on any traversal sequences.
* It's also possible to employ nested traversal sequences like `"....//"` or `"....\/"`to bypass defenses that  block simple traversal sequences. These nested sequences work by appearing harmless at first glance but revert to standard traversal sequences once the inner sequence is stripped, allowing attackers to navigate through directory structures and access sensitive files despite attempts to filter out traversal attempts. 