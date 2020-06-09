from cryptography.fernet import Fernet
import os
import sys
cmd = 'git clone git@github.com:skaushikpowershell/Key.git'
os.system(cmd)
with open (r"C:\Users\Kaushik Seetharam\python_codes\Programming\encryption_decryption\key.txt", "r") as myfile:
    encryppasswd=myfile.readlines()
encryppasswd = ' '.join(map(str, encryppasswd))     
bytessencryppasswd = bytes(encryppasswd, 'utf-8')
print (bytessencryppasswd)
#encryppasswd = b'gAAAAABe3kUIbTvxaNqhI9lQGtwrrzJsHiBHUb-crCqn2lTxMxSs37zM8CyLJG1qLI7Iy1dRMpP9VabSJSlzPPzs-nkldIcIsS7gYBk-5pEuWfs2XtFmFV0='
stringencryp = (str(encryppasswd))
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
cipher_suite = Fernet(key)
EncryptedPasswd = bytessencryppasswd
unciphered_text = (cipher_suite.decrypt(EncryptedPasswd))
string_unciphered_text = str(unciphered_text)
string_unciphered_text = string_unciphered_text.replace("'", "")
filtered_string_unciphered_text = string_unciphered_text[1:]
if filtered_string_unciphered_text == "SuperSecretPassword":
    print ('Match is Successful')
else:
    print ('failure')
#import os
#cmd = 'rmdir /Q /S "C:\\Users\\Kaushik Seetharam\\python_codes\\Programming\\encryption_decryption\\Key"'
#os.system(cmd)
#print("File Removed!")
