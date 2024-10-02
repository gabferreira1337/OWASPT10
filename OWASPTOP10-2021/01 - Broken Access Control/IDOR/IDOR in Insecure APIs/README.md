# IDOR in Insecure APIs
***
#### Another common type of IDOR is the `IDOR Insecure Function Calls`, where we can call APIs or execute functions as another user.

### Identifying Insecure APIs
#### Imagine a scenario where a web application has an update profile feature, that it sends a **PUT** request to an api endpoint (e.g. /profile/api.php/profile/1).
#### Example of JSON parameters sent to that endpoint
```bash
{
    "uid": 1337,
    "uuid": "40f5888b67c748df7efba008e7c2f9d2",
    "role": "employee",
    "full_name": "Lorum Ipsum",
    "email": "l_ipsum@employees.leet",
    "about": "This is my about"
}
```
#### By checking each parameter we can find some that can be abused , for example the **uid** and **role** parameters.
#### Unless the web application has implemented a robust control system on the back-end, we should be able to set an arbitrary role for our user, and consequently grant us more privileges.

### Exploiting Insecure APIs
#### Through the PUT request above we can perform multiple changes to the parameters, for example:
1. Change our `uid` to another user's `uid`` to try and take over their accounts
2. Change another user's details, allowing us to perform several web attacks
3. Create new users with arbitrary details, or delete existing ones
4. Change our role to a more privileged role (e.g `admin`) to be able to execute more actions

#### Even when the web application its properly testing the `IDOR Insecure function Calls` we can try and test the API's `GET` request for `IDOR Information Disclosure Vulnerabilities`.
