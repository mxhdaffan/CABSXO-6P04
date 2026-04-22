import hashlib

message = input("Enter Message: ")
message_bytes = message.encode()        # Calculating bytes

hash_object = hashlib.sha256(message_bytes)
hash_value = hash_object.hexdigest()        # Converting hash to readable (Hexadecimal form)

print("Hash:", hash_value)