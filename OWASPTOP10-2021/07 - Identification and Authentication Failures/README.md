# [Identification and Authentication](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)
***
### Authentication vs Authorization
#### Authentication is the process of confirming an entity's identity, ensuring they are who they claim to be , while authorization determines what users can and cannot access .

### Common Authentication Methods
#### We can divide them ito the following major categories:
* Knowledge-based authentication
* Ownership-based authentication
* Inherence-based authentication

### Knowledge
#### Method of authentication based on te ***something you know*** factor, for example  passwords passphrases, PINs, or answers to security questions

### Ownership
#### Method of authentication based on the ***something you have*** factor, for instance, ID cards, security tokens, or smartphones with authentication apps.

### Inherence
#### Method of authentication based on the ***something you are*** factor, such as, ID cards, fingerprints, facial patterns, and voice recognition, or signatures.


### Single-Factor vs Multi-Factor Authentication
#### Single-factor authentication only uses a single method. 
#### On the other hand, MFA uses multiple authentication methods. For example, a login form that requires a password (**something you know**) and a time-based one time password (**something you have**).
#### When only 2 factors are required, such as the example above, MFA can be referred to as 2-Factor Authentication (2FA).

### Attacks on Authentication
### Attacking Knowledge-based Authentication
#### Knowledge-based authentication can be easy to attack by guessing , brute forcing, or social engineering . This happens, because it suffers from reliance on static personal information. 

### Attacking Ownership-based Authentication
#### Ownership-based authentication that are based on physical possession, are consequently more secured. However , systems using this authentication method can be vulnerable to physical attacks, such as stealing or cloning the object, and execute cryptographic attacks on the algorithm it uses.
#### One common attack vector involves cloning objects like NFC badges in public places

### Attacking Inherence-based Authentication
#### Inherence-based authentication system can be compromised by a data breach. This happens because users can't change their biometric features, such as fingerprints.

