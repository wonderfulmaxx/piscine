# from hashlib import sha1
# import hashlib
# import hmac
# import time


# with open("starting.key", "r") as file:
#     key = file.read()


# key_b = key.encode()
    
# timestamp = int(time.time()) // 100


# time_b = timestamp.to_bytes(8,'big')


# hmac_result = hashlib.sha1(key_b + time_b).digest()

# print(hmac_result)


import hmac
import hashlib

def generate_hmac_sha1(key, message):
    hmac_sha1 = hmac.new(key, message, hashlib.sha1)
    hmac_value = hmac_sha1.digest()
    return hmac_value

# Example usage
key = b"my_secret_key"
message = b"my_message"

hmac_sha1_value = generate_hmac_sha1(key, message)
print(hmac_sha1_value)  # Print the HMAC-SHA-1 value in hexadecimal format