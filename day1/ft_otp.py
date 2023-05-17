import hashlib
import hmac
from cryptography.fernet import Fernet
import sys
import os
import re
import time
import base64

def parsing(nb_args):
   counter = 1
   _k = False
   encrypt_key = None
   hexa_key = None
   _g = False

   if (nb_args == 1):
      print("Too few args")

   while counter < nb_args:
      if sys.argv[counter] == "-k":
         _k = True
         if counter + 1 is not nb_args - 1:
            print("please enter the encrypted key after -k")
            sys.exit(1)
         else:
            counter += 1
            if os.path.exists(sys.argv[counter]):
               with open(sys.argv[counter], 'r') as fichier:
                  encrypt_key = fichier.read()
            else:
               encrypt_key = sys.argv[counter]
           
      elif sys.argv[counter] == "-g":
         _g = True
         if counter + 1 is not nb_args - 1:
            print("please enter a key of 64 hexadecimal characters -g")
            sys.exit(1)
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
   return (_k,encrypt_key,hexa_key,_g)



file_key = Fernet(b"Dv8hYrTR2mR5iR486MD7GzZMmgCPdtG7l12DrayajQM=")

_k,encrypt_key,hexa_key,_g= parsing(len(sys.argv))

if _g:
   hexa_key= hexa_key.upper()
   encrypt_key = file_key.encrypt(hexa_key.encode())
   with open('./ft_otp.key', 'wb') as fichier:
      fichier.write(encrypt_key)
   print("Key saved in ft_otp.key")
if _k:
   try:
      hexa_key = file_key.decrypt(encrypt_key)
   except:
      print("Wrong key")
      sys.exit(1)
   hexa_key64 = base64.b16decode(hexa_key) # decode la base 16 et le met en base 64 pour le hmac
   time = time.time()
   arr_time = int(time)//30
   arr_time_bytes = arr_time.to_bytes(8, byteorder = 'big')  # conversion vers 64 bits avec octects triers en decroissant
   hashed = hmac.new(hexa_key64, arr_time_bytes, hashlib.sha1)
   digest= hashed.hexdigest() 
   offset = int(digest[-1],16)


   bin_code = bin(int(digest[offset*2:offset*2+8], 16)) #1a3a54f45c -> 011101010001
   if len(bin_code[2:]) > 31:
      otp = int(bin_code[3:], 2) % 1000000
   else:
      otp = int(bin_code[2:], 2) % 1000000
   print(str(otp).zfill(6))
