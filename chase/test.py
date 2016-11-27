import os
from gnupg.py import gnupg

os.system('rm -rf /home/Desktop/gpghome')
gpg = gnupg.GPG(gnupghome='/home/Desktop/gpghome')
input_data = gpg.gen_key_input(
    name_email='chasetoy9@gmail.com',
    passphrase='password')
key = gpg.gen_key(input_data)
print key
