# [File Inclusion](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion)
***
#### Many contemporary back-end languages like PHP, JavaScript, and Java use HTTP parameters to control what content is displayed on a webpage. This approach enables the creation of dynamic web pages, streamlines the code, and reduces its overall size. In these cases, parameters are used to determine which resources are loaded. However, if this functionality is not properly secured, an attacker could tamper with these parameters to access and display any local file on the server, resulting in a Local File Inclusion (LFI) vulnerability.
### Local File Inclusion
#### Through the exploitation of Local File Inclusion vulnerabilities it is possible to disclose source code,  sensitive data and even execute code remotely.

### Example of Vulnerable code
#### File inclusion vulnerabilities can occur in any of the most popular web servers and development frameworks, like **PHP**, **NodeJS**, **Java**, **.Net**, and others. Where each of them share the same principle of loading a file from a specified path. 
#### These files could be a dynamic header or other content based on the user-specified language. For instance, a page where the user can change the language (e.g `?language=pt`), by changing that value it could change the directory that the web application is loading the pages.

### PHP
#### In PHP, the `include()` function is used to load a local or remote file as the page is loaded. When the path inserted to the `include()` is from an input controlled by a user, and the code does not filter and sanitize the user input, then it becomes vulnerable to File Inclusion.
```php
if (isset($_GET['lang'])) {
    include($_GET['lang']);
}
```
#### As we can see the lang parameter is directly passed to the `include(`) function, where any path inputted in the lang parameter will be loaded on the page. Besides the `include()` function , there are many others that would lead to the same vulnerability  if we could control the path passed into them.
#### Example of such functions in PHP: `include_once`, `require_once`, `require`, `file_get_contents()`,    

### NodeJS
#### The above statement also applies to NodeJS functions used to load content based on an HTTP parameter.
```javascript
if(req.query.lang) {
    fs.readFile(path.join(__dirname, req.query.lang), function (err, data) {
        res.write(data);
    });
```

#### In the above example , the parameter passed from the URL gets used by the `readfile` function before writing the file content in the HTTP response. This can also be seen in the `Express.js` framework by using the `render()` function.
#### Example using the lang parameter to determine which directory it should pull the `about.hmtl` from:
```js
app.get("/about/:lang", function(req, res) {
    res.render(`/${req.params.language}/about.html`);
});
```
#### The above code takes the parameter from the URL path (e.g. `/about/en`) unlike the previous examples.

### Java
#### Example of how web applications for a Java web server may include files based on the specified parameter (using the ìnclude function):
```jsp
<c:if test="${not empty param.lang}">
    <jsp:include file="<%= request.getParameter('lang') %>" />
</c:if>
```
#### The above can also be achieved using the `import function`:
```jsp
<c:import url= "<%= request.getParameter('lang') %>"/>
```

### .NET
#### Lastly , the `Response.WriteFile` function in .NET works similarly to the previously mentioned functions , as it takes a file path for it input and write its content to the response.
```cs
@if (!string.IsNullOrEmpty(HttpContext.Request.Query['lang'])) {
    <% Response.WriteFile("<% HttpContext.Request.Query['lang'] %>"); %> 
}
```
#### In `.NET` , the `@Html.Partial()` function may also be used to render a specified file as part of the template:
```cs
@Html.Partial(HttpContext.Request.Query['lang'])
```

#### Or also the `include` function can be used to render local files or remote URLs, and execute the specified files.
```cs
<!--#include file="<% HttpContext.Request.Query['lang'] %>"-->
```

#### **NOTE**: Some functions only read the content of the specified files, while others also execute the specified files.

# File Inclusion Functions in Various Languages
This table summarizes the behavior of different file inclusion functions in PHP, NodeJS, Java, and .NET in terms of their ability to read content, execute the file, and include remote URLs.


| Language | Function                    | Read Content | Execute | Remote URL |
|----------|-----------------------------|--------------|---------|------------|
| PHP      | `include()` / `include_once()` | ✅            | ✅       | ✅          |
| PHP      | `require()` / `require_once()` | ✅            | ✅       | ❌          |
| PHP      | `file_get_contents()`         | ✅            | ❌       | ✅          |
| PHP      | `fopen()` / `file()`          | ✅            | ❌       | ❌          |
| NodeJS   | `fs.readFile()`               | ✅            | ❌       | ❌          |
| NodeJS   | `fs.sendFile()`               | ✅            | ❌       | ❌          |
| NodeJS   | `res.render()`                | ✅            | ✅       | ❌          |
| Java     | `include`                    | ✅            | ❌       | ❌          |
| Java     | `import`                     | ✅            | ✅       | ✅          |
| .NET     | `@Html.Partial()`             | ✅            | ❌       | ❌          |
| .NET     | `@Html.RemotePartial()`       | ✅            | ❌       | ✅          |
| .NET     | `Response.WriteFile()`        | ✅            | ❌       | ❌          |
| .NET     | `include`                    | ✅            | ✅       | ✅          |


---

### Key:
- ✅ : Supported
- ❌ : Not Supported
