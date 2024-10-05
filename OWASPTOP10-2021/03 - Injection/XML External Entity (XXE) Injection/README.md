# [XML External Entity (XXE) Injection](https://portswigger.net/web-security/xxe)
***
#### XXE Injection vulnerabilities happen when XML data is used from a user-controlled input without sanitization or safe parsing , allowing us to use XML features to perform attacks. This vulnerabilities can damage a web application and its back-end server, from disclosing information to DoS the server.
### XML
#### XML is a markup language made for the transfer and storage of data and documents.

#### Example of an XML document:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<email>
  <date>01-01-2024</date>
  <time>12:00 am UTC</time>
  <sender>leet@nothacking.com</sender>
  <recipients>
    <to>HR@nothacking.com</to>
    <cc>
        <to>billing@nothacking.com</to>
        <to>payslips@inothacking.com</to>
    </cc>
  </recipients>
  <body>
    Wazzup m8,
        Let's do some hacking?
  </body> 
</email>

```

* Tag: Keys of an XML document
  *  `<time>`
* Entity: XML Variables 
  *  `&lt`;
* Element: Value stored between a start-tag and an end-tag
  *  `<date>01-01-2024</date>`
* Attribute: Optional specifications
  * `version="1.0"/encoding="UTF-8"`
* Declaration: Defines XML version and encoding
  * `<?xml version="1.0" enconding="UTF-8"?>`

#### As some characters are used as part of an XML document structure, we need to replace them with their respective entity references (e.g. `<`= `&lt`;)

### XML Document Type Definition (DTD)
#### Validate an XML document comparing with a pre-defined document structure.
#### Example DTD for the XML document above
```xml
<!DOCTYPE email [
  <!ELEMENT email (date, time, sender, recipients, body)>
  <!ELEMENT recipients (to, cc?)>
  <!ELEMENT cc (to*)>
  <!ELEMENT date (#PCDATA)>
  <!ELEMENT time (#PCDATA)>
  <!ELEMENT sender (#PCDATA)>
  <!ELEMENT to  (#PCDATA)>
  <!ELEMENT body (#PCDATA)>
]>
```
#### The DTD shown is defining the root `email` element using an ELEMENT type declaration, followed by the specification of its child elements. Each of those child elements is then individually declared, with some containing further nested elements, while others are marked to hold plain text data, indicated by `PCDATA`.
#### This DTD can either be embedded directly inside the XML file immediately after the XML declaration. Alternatively, it can be saved separately in an external file (for instance, named `email.dtd`) and linked within the XML document using the `SYSTEM` keyword:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email SYSTEM "email.dtd">
```

#### Or reference through a URL:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email SYSTEM "http://vulnerablewebsite.com/email.dtd">
```

### XML Entities
#### It is also possible to define custom entities in XML DTDs. This can be achieved by using the `ENTITY` keyword followed by the entity name and its value:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email [
  <!ENTITY company "Vulnerable Company">
]>
```

#### After defining an entity we can reference it, in an XML document by using a an `&` and a `;` (e.g `&company;`). When an entity is referenced, it is replaced with its value by the XML parser. Moreover, we can `reference External XML Entities`with the `SYSTEM` keyword  followed by the external entity's path:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE email [
  <!ENTITY company SYSTEM "http://localhost/company.txt">
  <!ENTITY signature SYSTEM "file:///var/www/html/signature.txt">
]>

```

#### **NOTE:** Similarly to the `SYSTEM` keyword, we can also use the `PUBLIC` keyword to load external resources, as it is used with publicly declared entities and standards.

#### When the XML file is parsed on the server-side , such as SOAP APIs or web forms, then an entity can reference a file stored on the back-end server, which may eventually be disclosed to us when we reference the entity