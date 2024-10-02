# [Server-Side includes Injection (SSI) ](https://owasp.org/www-community/attacks/Server-Side_Includes_(SSI)_Injection)
***
#### Server-side includes (SSI) allow web servers to dynamically generate HTML by embedding directives within HTML files. These directives can, for example, include shared content like headers or footers across multiple pages. If an attacker is able to inject malicious commands into these SSI directives, it can lead to a Server-Side Includes (SSI) Injection. This vulnerability may result in data leaks or even enable the attacker to execute commands on the server, potentially compromising it.
#### SSI can be often inferred from the file extension. Typical file extensions include `.shtml`, `.shtm` and `.stm` .

### SSI Directives
#### Directives ar used to add dynamically generated content to a static HTML page. They are composed of:
* ***name***: the directive's name
* ***parameter name***: one or more parameters
* ***value***: one or more parameter values
#### Directive Syntax
```ssi
<!--#name param1="value1" param2="value" -->
```

#### Examples of common SSI directives:
#### ***printenv*** : print environment variables
```ssi
<!--#printenv -->
```
#### ***config*** : Change SSI configuration  by specifying corresponding parameters
```ssi
<!--#config errmsg="Error!" -->
```

#### ***echo*** : Print value/s from var parameter/s
#### Supported variables
* ***DOCUMENT_NAME***: the current file's name
* ***DOCUMENT_URI***: the current file's URI
* ***LAST_MODIFIED***: timestamp of the last modification of the current file
* ***DATE_LOCAL***: local server time

```ssi
<!--#echo var="DOCUMENT_NAME" var="DATE_LOCAL" -->
```

#### ***exec*** : Execute command given in the ***cmd*** parameter:
```ssi
<!--#exec cmd="whoami" -->
```

#### ***include*** : Include a file from the web root directory , by specifying in the **virtual** parameter.
```ssi
<!--#include virtual="index.html" -->
```
### SSI injection
#### It occurs when SSI directives are injected into a file that is afterwards served by the web server.
#### For example, a vulnerable file upload vulnerability that let an attacker to upload a file containing malicious SSI directives into the web root directory.
