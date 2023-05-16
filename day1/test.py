from cryptography.fernet import Fernet


#------------recuperation de starting--------#

with open("starting.key", "r") as file:
    key = file.read()


B = Fernet(key)   # on a la key


#------------recuperation de token (A)--------#

with open("a.key", "r") as file:
    token = file.read()





print(B.decrypt(token).decode())