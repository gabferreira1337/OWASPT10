# Authentication Bypass via Direct Access
***
### Direct Access
#### Direct access occurs when an unauthenticated attacker gains access to protected information, when a web application does not properly verify that the request is authenticated.
#### For example, an application that redirects users to the `/admin.php` endpoint after a successful authentication, if the web application relies solely on the login page to authenticate users, we could access the protected resource directly by accessing the `/admin.php` endpoint.
#### Example of a vulnerable PHP code to verify whether a user is authenticated.
```php
if(!$_SESSION['active']) {
	header("Location: index.php");
}
```
#### The code above redirects the user to `/index.php` if the session is not active ( i.e, if the user is not authenticated). However, the PHP script does not stop execution , resulting in protected information within the page being sent in the response bode.
#### While trying to access the admin page through the browser we see that we are redirected. We can easily bypass this by intercepting the response and changing the status code from 302 to 200. To achieve this, we can enable `Intercept` in Burp. Then , browse to the `/admin.php` endpoint in the web browser. Next , we right-click on the request and select `Do intercept > Response to this request` to intercept the response. Afterward, we forward the request by clicking on `Forward`. As we intercepted the response , we can now edit it. In order to the force the browser to display the content, we need to change the status code from `302 Found` to `200 OK`.
#### Finally , we can forward the response. If we switch back to pur browser window, we can see that the protected information is rendered.

#### To prevent the protected information from being returned in the body of the redirect response, the PHP script needs to exit after issuing the redirect
```php
if(!$_SESSION['active']) {
	header("Location: index.php");
	exit;
	}
```
