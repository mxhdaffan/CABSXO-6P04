from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = input("Enter key: ").encode().ljust(16, b' ')
cipher = AES.new(key, AES.MODE_ECB)

plaintext = input("Enter message: ").encode()
ciphertext = cipher.encrypt(pad(plaintext, 16))
print("\nEncrypted message:", ciphertext.hex())

decrypted = unpad(cipher.decrypt(ciphertext), 16)
print("\nDecrypted message:", decrypted.decode())