# Use of SQL in Web Applications
***
### Example in a PHP web application
```php
$conn = new mysqli("localhost", "root", "password", "users");
$query = "select * from users";
$result = $conn->query($quey);
```
### Web applications usually use user-input when retrieving data
#### Example with SQLi vulnerability (no sanitization):
```php
$searchInput = $_POST['findUser'];
$query = "select * from users where username like "%$searchInput"";
$result = $conn->query($quey);
```

#### Sanitization refers to the removal of any special characters in user-input, in order to break any injections attempts.
