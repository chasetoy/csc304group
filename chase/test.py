import os
import gnupg

os.system('rm -rf /home/testgpguser/gpghome')
gpg = gnupg.GPG(gnupghome='/home/testgpguser/gpghome')
input_data = gpg.gen_key_input(
    name_email='testgpguser@mydomain.com',
    passphrase='my passphrase')
key = gpg.gen_key(input_data)
print key
