from cryptography.fernet import Fernet
import pickle
import pyotp


#------------------- Starting --------------------------#




key = Fernet.generate_key()  



#----------------------- B --------------------------#


B = Fernet(key)    


#----------------------- A( = token) --------------------------#

token = B.encrypt("my deep dark secret".encode()) #encrypter le message avec B




#decription du token(A) grace a B

decrypted = B.decrypt(token)

print(decrypted)
print(decrypted.decode())




