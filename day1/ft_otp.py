from cryptography.fernet import Fernet
import pickle

#------------------- Starting --------------------------#

key = Fernet.generate_key()  

with open('starting.key', 'wb') as filekey:
   filekey.write(key)

#----------------------- B --------------------------#


B = Fernet(key)    

print ("b=",B)

with open('b.key', 'wb') as filekey:
   pickled_b = pickle.dumps(B)       #ne sert a rien, juste pour rendre le bail visuel
   filekey.write(pickled_b)


#----------------------- A( = token) --------------------------#

token = B.encrypt("my deep dark secret".encode()) #encrypter le message avec B



with open('a.key', 'wb') as filekey:  #ecrire le message crypter A
   filekey.write(token)


#decription du token(A) grace a B

decrypted = B.decrypt(token)

print(decrypted)
print(decrypted.decode())

