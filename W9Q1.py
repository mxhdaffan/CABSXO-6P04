import hashlib
msg = b"Hello World"
sha1_hash = hashlib.sha1(msg).hexdigest()
sha2_hash = hashlib.sha256(msg).hexdigest()
sha3_hash = hashlib.sha3_256(msg).hexdigest()
print("SHA-1:", sha1_hash)
print("SHA-2:", sha2_hash)
print("SHA-3:", sha3_hash)