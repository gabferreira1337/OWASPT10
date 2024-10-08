# Horizontal Privilege Escalation
***
### Horizontal privilege escalation occurs when a user gains access to information or resources of another user.
* Example: The account page of the current user on ``` https://example-1337.com/account?id=42.```
* An attacker can modify the **id** parameter value to another, attempting to gain access to another user's account page and retrieve all associated data.
***
### Horizontal to vertical privilege escalation
#### Frequently, a horizontal privilege escalation attack can be turned into a vertical privilege escalation, by compromising a more privileged user. For example, when the attacker executes a horizontal escalation he might exploit an administrator account and gain administrative access, performing a vertical privilege escalation

### Certain applications employ globally unique identifiers **(GUIDs)** rather than predictable, incrementing numbers as exploitable parameters for user identification, to prevent an attacker from easily guessing or predicting user identifiers. However, a potential security challenge arises when these GUIDs, associated with different users, are inadvertently revealed in various sections of the application, such as user messages or reviews.
