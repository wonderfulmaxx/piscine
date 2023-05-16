from cryptography.fernet import Fernet
import os

# Générer 32 octets aléatoires
key = os.urandom(32)

# Convertir la clé en format hexadécimal
hex_key = key.hex()

# Afficher la clé hexadécimale de 64 caractères
print(hex_key)