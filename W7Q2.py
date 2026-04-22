from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

key = input("Enter key: ").encode()     # takes input and converts to bytes
cipher = Blowfish.new(key, Blowfish.MODE_ECB)       # ElectronicCodeBook mode (independently encrypts each data block)

plaintext = input("Enter message: ").encode()
padded_text = pad(plaintext, Blowfish.block_size)       # Adjusts data according to block size
# "hello" → padded → "hello***"

ciphertext = cipher.encrypt(padded_text)
print("\nEncrypted message:", ciphertext.hex())

decrypted = cipher.decrypt(ciphertext)
print("Decrypted message:", unpad(decrypted, Blowfish.block_size).decode())     # unpad removes padding