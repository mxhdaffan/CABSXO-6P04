import hmac
import hashlib
key = b"secret_key"
message = b"Hello World"
hmac_value = hmac.new(key, message, hashlib.sha256).hexdigest()
print("HMAC:", hmac_value)