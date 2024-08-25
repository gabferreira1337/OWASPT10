# [Server-Side Template Injection (SSTI)](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server_Side_Template_Injection)
***
#### Web applications often use templating engines to dynamically create HTML content based on user input. If an attacker is able to insert malicious template code, it can exploit a Server-Side Template Injection (SSTI) vulnerability. This can result in serious security risks like data breaches or even allow the attacker to take control of the server through remote code execution.
### Template Engines
#### Combines predetermined templates with dynamically generated data.
#### Examples of template engines [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) and [Twig](https://twig.symfony.com/) .

### Templating
#### In order to use a template engine we would need a template and a set of values to be inputted into the template. We can provide a template as a string or a file, containing pre-defined places where template engines inserts the dynamically generated values. To provide values we need to use key-value pairs , in order to the template engine to place the given value at the exact location pointed with the respective key.
#### Rendering is the process of generating a string from the input template and input values
#### Example of a template string using `Jinja`
```jinja2
Hello {{ name }}!
```

#### The variable `name` will be replaced by a dynamic value on rendering.

#### Example using a for loop 
```jinja2
{% for name in names %}
Hello {{ name }}!
{% endfor %}
```

#### Template engines can work with user input securely if provided as values to the rendering function. Therefore, template engines insert the values into the respective places in the template and do not execute any code within the values.
#### SSTI occurs when it's possible to control the template parameter, as template engines execute the code provided in the template, or when user input is inserted ***before** the rendering function is called on the template.


## [SSTImap](https://github.com/vladko312/SSTImap)
## [PayloadsAllTheThings SSTI CheatSheet](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md)