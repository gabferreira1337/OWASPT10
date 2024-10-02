# Chaining IDOR Vulnerabilities
***

### Information Disclosure
#### First we send a **GET** request to an API endpoint with an arbitrary value, for instance with another **uid**
```json
{
    "uid": "4",
    "uuid": "7b9bd12f3b8676179192a347051f987c",
    "role": "employee",
    "full_name": "Java Chip",
    "email": "j_chip@employees.leet",
    "about": "A cookie a day ..."
}
```
#### As we can see , by executing a GET request it provided us with new details of another user, especially the **uuid** that cannot be changed.

### Modifying Other Users' Details
#### With the **uuid** in our side we can try to send a `PUT` request to that same API endpoint (e.g `/profile/api.php/profile/4`) with all the modifications that we want to execute.
#### Furthermore, the ability to modify another user's details also enables us to perform several other attacks, one of which is `modifying a user's email address` to request a password reset to our email. Additionally, we may try to `place an XSS payload in the 'about' field`, that consequently would be executed once every user visits their profile page, enabling us to attack the user in different ways.

### Chaining Two IDOR Vulnerabilities
#### After identifying an IDOR Information Disclosure vulnerability, we may also enumerate all users and look for other **roles**, like an admin role with more privileges.
#### Example of an Admin User information
```json
{
    "uid": "Z",
    "uuid": "f56ba9e66e85a2de6f5b13eed41278aa",
    "role": "web_admin",
    "full_name": "administrator",
    "email": "webadmin@employees.leet",
    "about": "I'm not an admin **wink** **wink**"
}
```

#### We may change the admin's details and then perform one of the mentioned attacks above to take over their account. However , as we now know the admin role name (`web_admin`) , we can insert it in our user to be able to perform admin functions , such as create a new user or delete a current one.
```json
{
    "uid": "1",
    "uuid": "51d5877b67e748ab7efba128e7c6e4a1",
    "role": "employee",
    "full_name": "web_admin",
    "email": "m_account@employees.leet",
    "about": "I wish I was an admin ~-_-~"
}
```

