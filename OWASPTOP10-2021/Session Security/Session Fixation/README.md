# Session Fixation
***
#### Session Fixation is a type of attack where we trick a user into using a known or predetermined session ID. Once the user authenticates using this session ID, we can hijack the session and gain unauthorised access.
#### This is commonly seen when session IDs are being accepted from URL Query Strings or Post Data.

### Example:
* Firstly we obtain a valid session ID.
* Secondly we fixate a valid session ID.
#### The session fixation vulnerability can arise when the assigned session ID pre-login remains the same post-login. 
#### Additionally, it is also possible to exploit that vulnerability when session IDs are being accepted from URL Query Strings or Post Data and propagated to the application.
* Finally, we trick our target into establishing a session using our session ID 


#### Example of a vulnerable code
```php
<?php
    if (!isset($_GET["token"])) {
        session_start();
        header("Location: /?redirect=/login.html&token=" . session_id());
    } else {
        setcookie("PHPSESSID", $_GET["token"]);
    }
?>
```