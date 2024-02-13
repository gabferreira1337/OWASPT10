# Horizontal Privilege Escalation
***
### Horizontal privilege escalation occurs when a user gains access to information or resources of another user.
* Example: The account page of the current user on https://example-1337.com/account?id=42.
* An attacker can modify the **id** parameter value to another, attempting to gain access to another user's account page and retrieve all associated data.
***
### 3 Best practices to avoid horizontal privilege escalation:
* **Secure Session Management**: Secure session handling practices , including session timeouts, token validation.For example: Invalidate sessions promptly after users log out
or when they are inactive for a predefined period.
* **Principle of Least Privilege (PoLP)**: Limit user privileges to the minimum necessary for their tasks. Avoid giving users more access than required , and regularly review and update access permissions
* **Regular Monitoring**: Continuously monitor user activities and network traffic for anomalies. Use intrusion detection systems **(IDS)** or security information event management **(SIEM)** tools to identify unusual patterns or behaviors.

***
***Note:*** Certain applications employ globally unique identifiers **(GUIDs)** rather than predictable, incrementing numbers as exploitable parameters for user identification, to prevent an attacker from easily guessing or predicting user identifiers.
However, a potential security challenge arises when these GUIDs, associated with different users, are inadvertently revealed in various sections of the application, such as user messages or reviews.
