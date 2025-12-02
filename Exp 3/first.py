import random
import hashlib


shared_secret_key = "Hello"


def nonce_generate():
    return random.randint(1000, 9999)


print(f"The Nonce is: {nonce_generate()}")

mixing = shared_secret_key + str(nonce_generate())
# Client side

client_hash = hashlib.sha256(mixing.encode()).hexdigest()

print(f"Client hash is : {client_hash}")

# compairing
server_hash = hashlib.sha256(mixing.encode()).hexdigest()

print(f"Server hash is : {server_hash}")

# comparing

check_hash = client_hash == server_hash

print(check_hash)
