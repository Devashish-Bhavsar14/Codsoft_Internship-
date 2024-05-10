import random 
import string

DIGITS = string.digits   
LOCASE_CHARACTERS =string.ascii_lowercase
  
UP_CHARACTERS =string.ascii_uppercase
SYMBOLS =string.punctuation
all_keys=DIGITS+LOCASE_CHARACTERS+UP_CHARACTERS+SYMBOLS

password_len=int(input("enter the number: "))

password = ''
for i in range(password_len):
 password += ''.join(random.choice(all_keys))

print(f"the random generated password is {password}")