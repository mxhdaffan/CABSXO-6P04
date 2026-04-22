from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

message = b"Hello World"

# Generate RSA keys
key = RSA.generate(1024)
private_key = key
public_key = key.publickey()

# Hash the message
h = SHA256.new(message)

# Sign the message
signature = pkcs1_15.new(private_key).sign(h)

print("Digital Signature:", signature)