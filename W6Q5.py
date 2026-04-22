def F(right, key):
    return right ^ key

def encrypt(block, keys):
    left = block >> 4        
    right = block & 0b1111 

    for k in keys:
        new_left = right
        new_right = left ^ F(right, k)
        left, right = new_left, new_right

    return (left << 4) | right

def decrypt(block, keys):
    left = block >> 4
    right = block & 0b1111

    for k in reversed(keys):
        new_right = left
        new_left = right ^ F(left, k)
        left, right = new_left, new_right

    return (left << 4) | right

plaintext = int(input("Enter 8-bit plaintext (0-255): "))

keys = [3, 5, 7]

cipher = encrypt(plaintext, keys)
print("Encrypted:", cipher)

decrypted = decrypt(cipher, keys)
print("Decrypted:", decrypted)