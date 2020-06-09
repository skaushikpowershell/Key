from cryptography.fernet import Fernet
import os
import sys
cmd = 'git clone git@github.com:skaushikpowershell/Key.git'
os.system(cmd)
encryppasswd = b'gAAAAABe3kUIbTvxaNqhI9lQGtwrrzJsHiBHUb-crCqn2lTxMxSs37zM8CyLJG1qLI7Iy1dRMpP9VabSJSlzPPzs-nkldIcIsS7gYBk-5pEuWfs2XtFmFV0='
print (encryppasswd)
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
cipher_suite = Fernet(key)
EncryptedPasswd = encryppasswd
unciphered_text = (cipher_suite.decrypt(EncryptedPasswd))
string_unciphered_text = str(unciphered_text)
string_unciphered_text = string_unciphered_text.replace("'", "")
filtered_string_unciphered_text = string_unciphered_text[1:]
if filtered_string_unciphered_text == "SuperSecretPassword":
    print ('Match is Successful')
else:
    print ('failure')


