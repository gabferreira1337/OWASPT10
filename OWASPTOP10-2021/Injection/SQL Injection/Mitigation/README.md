# Mitigating SQL Injections
***
### Input Sanitization
#### Example of vulnerable PHP script
```php
<SNIP>
  $username = $_POST['username'];
  $password = $_POST['password'];

  $query = "SELECT * FROM logins WHERE username='". $username. "' AND password = '" . $password . "';" ;
  echo "Executing query: " . $query . "<br /><br />";

  if (!mysqli_query($conn ,$query))
  {
          die('Error: ' . mysqli_error($conn));
  }

  $result = mysqli_query($conn, $query);
  $row = mysqli_fetch_array($result);
<SNIP>
```

#### We can check on the script above that it takes in the username and password fom POST request and passes it to the query directly. Letting any attacker execute SQLi freely.
#### SQli can be avoided by sanitizing any user input. There are several libraries that provide functions to achieve that, one example is the **mysqli_real_escape_string()**
#### This function escapes characters such as ' and ", so they don't hold any special meaning.

```php
<SNIP>
$username = mysqli_real_escape_string($conn, $_POST['username']);
$password = mysqli_real_escape_string($conn, $_POST['password']);

$query = "SELECT * FROM logins WHERE username='". $username. "' AND password = '" . $password . "';" ;
echo "Executing query: " . $query . "<br /><br />";
<SNIP>
```

### Another good example is the pg_escape_string() which used to escape PostgreSQL queries.

### Input validation
#### User inout can also be validated based on the data used to query to ensure it matches the expected input.
#### Example of a vulnerable PHP script:
```php
<?php
if (isset($_GET["port_code"])) {
	$q = "Select * from ports where port_code ilike '%" . $_GET["port_code"] . "%'";
	$result = pg_query($conn,$q);
    
	if (!$result)
	{
   		die("</table></div><p style='font-size: 15px;'>" . pg_last_error($conn). "</p>");
	}
<SNIP>
?>
```

#### By looking at the script above we see that the GET parameter **port_code** is being used in the query directly. We can restrict the user input to only use certain characters, preventing the injection of queries.
#### Example using a regular expression (/^[A-Za-z\s]+) regex for strings only containing letters and spaces
```php
<SNIP>
$pattern = "/^[A-Za-z\s]+$/";
$code = $_GET["port_code"];

if(!preg_match($pattern, $code)) {
  die("</table></div><p style='font-size: 15px;'>Invalid input! Please try again.</p>");
}

$q = "Select * from ports where port_code ilike '%" . $code . "%'";
<SNIP>
```

#### In the script above we also used the preg_match() function to check if the input matches the given patter or not. 

### User privileges
#### Superusers and users with admin privileges should never be used with web applications
#### Example of adding a new MariaDB user with only SELECT privileges on a given table
```sql
MariaDB [(none)]> CREATE USER '1337'@'localhost';
MariaDB [(none)]> GRANT SELECT ON mydb.ports TO '1337'@'localhost' IDENTIFIED BY 'rootP';
```

### Web application Firewall (WAF)
#### WAFs are used to detect malicious input and reject any HTTP requests containing them. 
#### Examples of WAFs: ModSecurity (Open-source) , Cloudflare (premium)

### Parameterized Queries
#### Another way to ensure input safety is by using parameterized queries. With parameterized queries,  we don't directly insert user input into the SQL query. Instead, we use placeholders within the query, and the input data is then safely inserted by the database driver. The driver automatically handles the escaping and sanitization of the input, reducing the risk of SQL injection attacks. In PHP, funcitons are used to bind the actual user input to these placeholders before executing the query
#### Example:
```php
<SNIP>
  $username = $_POST['username'];
  $password = $_POST['password'];

  $query = "SELECT * FROM logins WHERE username=? AND password = ?" ;
  $stmt = mysqli_prepare($conn, $query);
  mysqli_stmt_bind_param($stmt, 'ss', $username, $password);
  mysqli_stmt_execute($stmt);
  $result = mysqli_stmt_get_result($stmt);

  $row = mysqli_fetch_array($result);
  mysqli_stmt_close($stmt);
<SNIP>
```
#### The query is updated to include two placeholders, represented by `?`, where the username and password will be inserted. We then use the `mysqli_stmt_bind_param()`function to link the actual username and password values to these placeholders. This  method ensures that any potentially harmful characters, like quotes, are properly escaped before being added to the query, providing a safer way to handle user input

