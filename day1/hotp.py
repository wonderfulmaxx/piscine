import hashlib
import time
import hmac

# Fonction pour générer un TOTP
def generate_totp(secret_key):

	interval = 30 # Intervalle en secondes pour le TOTP

	# print ("time =" , time.time())

    # Calcul du compteur (timestamp)
	timestamp = int(time.time()) // interval

	# print ("time//interval =" , timestamp)

	counter = timestamp.to_bytes(8, 'big')  # Convertir le timestamp en octets

	# print("counter =" , counter)

	counter_bytes = counter.rjust(8, b'\0')  # Remplir avec des octets nuls si nécessaire

	# print("counter_bytes =" , counter_bytes)
	# print("key = ", secret_key)
    # Calcul du HMAC-SHA1
	# hmac_result = hashlib.sha1(secret_key + counter_bytes).digest()
	hmac_result = hmac.new(secret_key, counter_bytes, hashlib.sha1).digest()

	print ("hmac_result = " , hmac_result)
	# print ("hmac_result2= " , hmac_result2)

    # Récupération de l'offset et génération de l'OTP
	offset = hmac_result[-1] & 0x0F  # Dernier octet du résultat HMAC

	# print ("offset=" , offset)

	otp = (int.from_bytes(hmac_result[offset:offset + 4], 'big') & 0x7FFFFFFF) % 1000000  # Générer un OTP à 6 chiffres

	# print ("otp=" , otp)

	return str(otp).zfill(6) 



# Clé secrète partagée entre le client et le serveur
secret_key = b'1a4b583e2fd85193b285e501d7044809d9d5df8189b2f23c10b358fe2a2ef5dd'

# Générer un TOTP
totp = generate_totp(secret_key)
print("TOTP:", totp)
