# Identifying IDORs
***
### URL Parameters and APIs
#### Firstly , in order to exploit IDOR vulnerabilities we should identify **Direct Object References** by checking the HTTP requests to look for URL parameters or APIs with an object reference (e.g. `?uid=1337` or `?filename=file_-1337.pdf`). We can find these parameters not only in URL parameters or APIs but also in other HTTP header, such as cookies.
#### Then in some cases we can try incrementing the values of the object reference to get other data. Furthermore, we can also try and fuzz those references and check if it returns any data. When we get any access to data that we don't own it would indicate an IDOR vulnerability.

### AJAX Calls
#### It is also possible to identify unused parameters or APIs in the front-end code in the form or JavaScript AJAX calls. Moreover, some web applications developed in JavaScript frameworks may insecurely place all function calls on the front-end using them based on the user role.

```javascript
function changeUserPassword() {
    $.ajax({
        url:"change_password.php",
        type: "post",
        dataType: "json",
        data: {uid: user.uid, password: user.password, is_admin: is_admin},
        success:function(result){
            //
        }
    });
}
```
#### If we've found in the front-end code a similar function as the above , we could test that to see whether we can call it to perform changes, which would indicate that it is vulnerable to IDOR. This method can also be applied to back-end code when we got access to it.

### Hashing/Encoding
#### Some web applications may encode the reference or hash it instead of simply relying on sequential numbers as object references. For example, when the object reference is hashed like (`download.php?fn=5db1fee4b5703808c48078a76768b155`), we can try and look for the source code or use tools to identify which hash algorithm its being used. With that we can use it to recalculate all the potential filenames for other files.
```javascript
$.ajax({
    url: "download.php",
    type: "post",
    dataType: "json",
    data: { 
        filename: CryptoJS.SHA256('file_1337.pdf').toString(CryptoJS.enc.Hex) 
    },
    success: function(result){
        // Handle success
    }
});

```

### Compare User Roles
#### To execute more advanced techniques to find IDOR vulnerabilities, we may need to register multiple users and compare their HTTP requests and object references, allowing us to understand hoe the URL patrameters and unique identifiers are being calculated and then calculate them for other users to gather their data.
#### For instance, if we got access to two unique users, one of which can view their salary after making the following API call:
```json
{
  "attributes" : 
    {
      "type" : "salary",
      "url" : "/services/data/salaries/users/1337"
    },
  "Id" : "1337",
  "Name" : "User1337"

}
```
#### The second user might not have access to all the API parameters needed to replicate the call made by User1. However, we can attempt to make the same API request while logged in as User2 to check if the web application returns a response. This could happen if the application only requires a valid session to process the API call but lacks proper back-end access controls to verify that the session matches the data being requested.
#### If this works, and we can identify or predict the API parameters for other users, this would indicate an Insecure Direct Object Reference (IDOR) vulnerability. Even if we can't figure out the exact parameters for other users, it would still reveal a weakness in the back-end's access control system, prompting further investigation into other potential object references that could be exploited.
