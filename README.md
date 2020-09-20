# share_secrets
A Simple crossplatform Secret sharing Tool using python3 . Initially Project Idea was Inspired by Samir Secret Sharing Scheme ssss debian package. This tool Can also be used as offline Password Backup System. 

Working:-

1) Converts your secret/password to random unguessable backup codes. Limitations currently only maximum 10 shares/codes and minimum 2 shares is allowed.

2) Reconstructs your secret/password from your backup codes on Demand.

Properties:-

The secret/password cannot be constructed even if one among the backup codes is missing.

Even for the same secret new unguessable codes are generated each time for security reasons. 

NOTE: Don't use this program in high risky situations or for any sensitive purpose. DEVELOPER NOT RESPONSIBLE FOR ANY DAMAGES ARISING FROM USE OF THIS SOFTWARE.

You can get my public OPENPGPKEY from here: https://outflaw.blogspot.com/2019/12/my-pgp-key.html incase you want to verify this software for more security.

Quick Installation
------------------

Install from [PyPI](https://pypi.org/project/share-secrets/):

```
pip install share-secrets
```
Then run following commands in terminal/powershell to get started:-

For Windows:
```
py -m share_secrets 
```
For Linux based Distributions:
```
python3 -m share_secrets
```

Contribute to share-secrets
---------------------------
Currently i consider this as a personal project so i dont expect public contributions.
Feel free to open issues if something breaks or for feature request. 



