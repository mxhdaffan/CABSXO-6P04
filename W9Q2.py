import hashlib
msg = b"Hello World"
md5_hash = hashlib.md5(msg).hexdigest()
print("MD5 Hash:", md5_hash)