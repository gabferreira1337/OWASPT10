# Broken Access Control


### Broken access control resulting from URL-matching discrepancies
#### Differences in how websites interpret incoming request paths can lead to inconsistencies in enforcing access control. 
#### For instance, some sites might overlook variations in capitalization, allowing requests lie `/ADMIN/ADDUSER` to still access the `/admin/addUser` endpoint. 
#### Similarly, developers using the **Spring** framework ,may enable an option called **useSuffixPatternMatch**, which permits requests with arbitrary file extensions to match endpoints without extensions, such as `/admin/addUser.anything`
#### Another potential inconsistency arises in how systems handle trailing slashes in paths, where `/admin/adminUser`  and `/admin/addUser/` might be treated differently.
#### Exploiting these discrepancies could allow users to bypass access controls by adding or removing trailing slashes from the request path
### 3 Best practices to avoid Broken access control:
***
* **Secure Session Management**: Secure session handling practices , including session timeouts, token validation.For example: Invalidate sessions promptly after users log out
or when they are inactive for a predefined period.
* **Principle of Least Privilege (PoLP)**: Limit user privileges to the minimum necessary for their tasks. Avoid giving users more access than required , and regularly review and update access permissions
* **Regular** Monitoring: Continuously monitor user activities and network traffic for anomalies. Use intrusion detection systems **(IDS)** or security information event management **(SIEM)** tools to identify unusual patterns or behaviors.