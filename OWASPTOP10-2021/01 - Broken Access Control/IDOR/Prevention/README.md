# IDOR Prevention
****
#### IDOR vulnerabilities typically arise when there are no proper access controls implemented on the back-end server. We should develop an object-level access control system and then use secure references for our objects when calling and storing them.

### Object-Level Access Control
#### To prevent IDOR vulnerabilities we need to set user roles and permissions, these are a key part of any access control system, which is fully implemented in a RBAC system. We must map the RAC to all objects and resources. The back-end server can allow or deny every request, depending on whether the requesters role has enough privileges to access the object or the resource.
#### There are several ways to implement an RBAC system and link it to the web application's objects and resources, but it is an art to perfect as it is really hard to implement.
#### Example of how a web application may compare user roles to objects to allow or deny access control:
```javascript
match /api/profile/{userId} {
    allow read, write: if user.isAuth == true
    && (user.uid == userId || user.roles == 'admin');
}
```
#### As we can see , the example above uses the **user** token , which can be mapped from the HTTP request made to the RBAC to retrieve the user's various roles and privileges. Moreover, it only allows read/write access if the user's **uid** in the RBAC system matches the **uid** in the API endpoint they're requesting.
#### This is a safer approach to map user roles because the `user privileges are not being passed through the HTTP request`. They are being mapped directly from the RBAC on the back-end using the user's logged-in session token as an authentication mechanism.

### Object Referencing
#### The core issue with IDOR (Insecure Direct Object Reference) stems from inadequate access control. When systems allow direct access to object references, attackers can potentially manipulate these references to access data they aren't authorized to see. However, direct object references can still be used safely if proper access control mechanisms are in place.
#### Even with a robust access control system, it’s important to avoid using object references in clear or predictable formats (like uid=1), which can easily be guessed or enumerated. Instead, we should use complex, unique identifiers like salted hashes or UUIDs. For instance, a UUID (Universally Unique Identifier) version 4 generates a highly randomized ID that looks like this: 67c9b31d-d27a-4515-b2dd-abb6e693eb11. This unique identifier is then mapped to the corresponding object in the database. When the UUID is requested, the system identifies the appropriate object on the backend and returns the correct data.
#### This approach ensures that even if an ID is exposed, it is difficult to guess or exploit without proper authorization, adding an extra layer of security against IDOR vulnerabilities. 
#### Here’s a simplified example of how this might be implemented in PHP:
```javascript
$uid = intval($_REQUEST['uid']);
$query = "SELECT url FROM documents where uid=" . $uid;
$result = mysqli_query($conn, $query);
$row = mysqli_fetch_array($result));
echo "<a href='" . $row['url'] . "' target='_blank'></a>";
```

#### Also, we should never calculate hashes on the front-end. We should generate them when an object is created and store them in the back-end database. Additionally , we should create database maps to enable quick cross-referencing of objects and references.
#### Lastly, by using **UUIDs**  (Universally Unique Identifier) may let IDOR vulnerabilities go undetected since it makes it harder to test for those type of vulnerabilities. This is the main reason to implement a strong object referencing after a strong access control system.
