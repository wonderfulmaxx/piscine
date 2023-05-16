import hashlib
import hmac
from cryptography.fernet import Fernet
import sys
import os
import re
import base64
import binascii

def parsing(nb_args):
   counter = 1
   generate = False
   encrypt_key = None
   hexa_key = None
   save = False
   generate_key = False

   if (nb_args == 1):
      print("Too few args")

   while counter < nb_args:
      if sys.argv[counter] == "-k":
         generate = True
         if counter + 1 is not nb_args - 1:
            print("please enter only an encrypted key after -k")
            sys.exit(1)
         else:
            counter += 1
            if os.path.exists(sys.argv[counter]):
               with open(sys.argv[counter + 1], 'r') as fichier:
                  encrypt_key = fichier.read()
            else:
               encrypt_key = sys.argv[counter]
           
      elif sys.argv[counter] == "-g":
         save = True
         if counter + 1 == nb_args:
            generate_key = True
         else:
            counter += 1
            if os.path.exists(sys.argv[counter]):
               with open(sys.argv[counter], 'r') as fichier:
                  hexa_key = fichier.read()
            else:
                  hexa_key = sys.argv[counter]
         motif = r'^[0-9a-fA-F]{64}$'
         if hexa_key is not None and not re.match(motif, hexa_key):
            print ("The key must be a key of 64 hexadecimal characters")
            sys.exit(1)

      else:
         print("Unavailable argument detected")
         sys.exit(1)
      counter += 1
   return (generate,encrypt_key,hexa_key,save,generate_key)




# def save_encryted_key(hexa_key64):
#    encrypted_key = Fernet(hexa_key64)
#    with open('./ft_otp.key', 'wb') as fichier:
#          fichier.write(encrypt_key)
   



generate,encrypt_key,hexa_key,save,generate_key= parsing(len(sys.argv))

if save:
   if generate_key:
      encrypt_key = Fernet.generate_key()

