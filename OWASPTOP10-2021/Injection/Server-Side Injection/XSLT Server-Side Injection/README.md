# [Extensible Stylesheet Language Transformations Server-Side Injection (XSLT)]()
***
#### XSLT (Extensible Stylesheet Language Transformations) server-side injection is a vulnerability that occurs when attackers manipulate XSLT transformations carried out on the server. XSLT is used to convert XML documents into other formats, like HTML, often for dynamic content generation in web applications. If vulnerabilities exist in how these transformations are processed, attackers can inject and execute arbitrary code on the server, potentially leading to severe security issues such as unauthorized access or server compromise.

### XSLT
#### XSLT is a language used to transform XML documents. For example, it can select nodes from an XML document and change the XML structure.
#### Example of XSLT operation
```xml
<?xml version="1.0" encoding="UTF-8"?>
<products>
    <product>
        <name>Milk</name>
        <color>White</color>
        <size>Medium</size>
    </product>
    <product>
        <name>Cocoa</name>
        <color>Brown</color>
        <size>Medium</size>
    </product>
    <product>
        <name>Lemon Tea</name>
        <color>Yellow</color>
        <size>Small</size>
    </product>
</products>
```
#### With XSLT we can define a data format that is subsequently enriched with data from the XML document.
#### XSL elements are prefixed with the `xsl`-prefix.
#### Examples of XSL elements:
* ***<xsl:template>***: This element indicates an XSL template. It can contain a match attribute that contains a path in the XML document that the template applies to
* ***<xsl:value-of>***: This element extracts the value of the XML node specified in the select attribute
* ***<xsl:for-each>***: This element enables looping over all XML nodes specified in the select attribute

#### For instance, a simple XSLT document usd to output all products contained within the XML document.
```xml
<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/products">
		Here are all the products:
		<xsl:for-each select="product">
			<xsl:value-of select="name"/> (<xsl:value-of select="color"/>)
		</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>

```
#### The XSLT document above contains a single `xsl:template` that is applied to the `products` node in the XML document.
#### Additional XSL elements to limit  further or customize the data from an XML document:
* ***<xsl:sort>***: This element specifies how to sort elements in a for loop in the select argument. Additionally, a sort order may be specified in the order argument
* ***<xsl:if>***: This element can be used to test for conditions on a node. The condition is specified in the test argument.

#### We can use the above XSL elements to  create a list of all products that are of a certain size ordered by their color in descending order:
```xml
<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/products">
		Here are all products of medium size ordered by their color:
		<xsl:for-each select="product">
			<xsl:sort select="color" order="descending" />
			<xsl:if test="size = 'Medium'">
				<xsl:value-of select="name"/> (<xsl:value-of select="color"/>)
			</xsl:if>
		</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>
```

### XSLT Injection
#### Occurs when user input is injected into XSL data before output generation by the XSLT processor.



