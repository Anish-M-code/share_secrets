# Pysecret
A Simple crossplatform Secret sharing Tool using python3 . Inspired by Samir Secret Sharing Scheme ssss debian package.
It Can even be used as offline stateless Password Backup System. 

Working:-

1) Converts your secret to random unguessable backup codes. Limitations only maximum 10 shares/codes and minimum 2 shares is allowed.

2)Reconstructs your secret from your backup codes on Demand.

Properties:-

The secret cannot be constructed even if one among the backup codes is missing.

For security reasons even for the same secret new unguessable codes are generated each time for security reasons. 
