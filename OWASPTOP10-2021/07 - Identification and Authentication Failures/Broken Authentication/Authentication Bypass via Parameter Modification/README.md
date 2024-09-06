# Authentication Bypass via Parameter Modification
***
#### When an authentication application depends on the presence or value of an HTTP parameter, it introduces an authentication vulnerability .
### Parameter Modification
#### For instance, a web application that after logging in, it redirects us to `/admin.php?user_id=123`.
#### Assuming that the  parameter `user_id` is related to authentication. We can bypass authentication by accessing the URL `/admin.php?userid=123`
#### Furthermore , we can execute a brute-force attack on that parameter to obtain an administrator ID . Then, we can obtain admin privileges (vertical privilege escalation) by specifying the admin's user ID in the `user_id` parameter.

