# Broken Access Control
***
### Broken access control resulting from URL-matching discrepancies
#### Differences in how websites interpret incoming request paths can lead to inconsistencies in enforcing access control. 
#### For instance, some sites might overlook variations in capitalization, allowing requests lie `/ADMIN/ADDUSER` to still access the `/admin/addUser` endpoint. 
#### Similarly, developers using the **Spring** framework ,may enable an option called **useSuffixPatternMatch**, which permits requests with arbitrary file extensions to match endpoints without extensions, such as `/admin/addUser.anything`
#### Another potential inconsistency arises in how systems handle trailing slashes in paths, where `/admin/adminUser`  and `/admin/addUser/` might be treated differently.
#### Exploiting these discrepancies could allow users to bypass access controls by adding or removing trailing slashes from the request path
***
#### Access control vulnerabilities can also arise in **multi-step** processes on websites when certain steps lack proper access controls. These process often involve capturing various inputs or options from users and requiring them to review and confirm details before proceeding.
#### For instance, consider an administrative function to update user details, which typically involves several steps:
1. Loading the form with user details.
2. Submitting the changes.
3. Renewing and confirming the changes.
#### While websites may enforce strict access controls on the first two steps, they sometimes overlook the third step. They may assume that users can only reach step 3 after completing the preceding steps, which are properly controlled. However, this assumption creates a vulnerability. An attacker can exploit this by bypassing the first two steps and directly submitting the request for the third step with the necessary parameters, allowing the attacker to gain unauthorized access to the function. 
### Referer-based access control
#### Certain websites use the **Referer** header in HTTP requests as a basis for access control. This header, automatically included by browsers, indicates the webpage that triggered the request. For example, while the main administrative page `admin` might have robust access control measures, sub-pages like `/admin/updateUser` may rely solely on the **Referer** header. If this header contains the main `/admin` URL, the request is granted. However, since attackers can manipulate the **Referer** header, they can forge requests to sensitive sub-pages by supplying the appropriate **Referer** header, thus gaining unauthorized access.

### 3 Best practices to avoid Broken access control:
***
* **Secure Session Management**: Secure session handling practices , including session timeouts, token validation.For example: Invalidate sessions promptly after users log out
or when they are inactive for a predefined period.
* **Principle of Least Privilege (PoLP)**: Limit user privileges to the minimum necessary for their tasks. Avoid giving users more access than required , and regularly review and update access permissions
* **Regular** Monitoring: Continuously monitor user activities and network traffic for anomalies. Use intrusion detection systems **(IDS)** or security information event management **(SIEM)** tools to identify unusual patterns or behaviors.