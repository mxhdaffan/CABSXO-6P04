from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

pr = rsa.generate_private_key(public_exponent=65537, key_size=2048)
pu = pr.public_key()

msg = b"asad"

# Create Digital Signature
sig = pr.sign(msg,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256())

try:
    pu.verify(sig, msg,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256())
    print("Valid signature")
except:
    print("Invalid signature")