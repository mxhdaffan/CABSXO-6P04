text = str(input("Enter plaintext: "))
shift = int(input("Enter shift value: "))
cipher = ""

for x in text:
    if(x.isalpha()):
        if(x.isupper()):
            cipher += chr((ord(x) + shift - ord('A'))%26 + ord('A'))
        else:
            cipher += chr((ord(x) + shift - ord('a'))%26 + ord('a'))
    else:
        cipher += x

print("\nEncrypted: ", cipher)

plain = ""
for y in cipher:
    if(y.isalpha()):
        if(y.isupper()):
            plain += chr((ord(y) + shift - ord('A'))%26 + ord('A'))
        else:
            plain += chr((ord(y) + shift - ord('a'))%26 + ord('a'))
    else:
        plain += y
        
print("Decrypted: ", plain)