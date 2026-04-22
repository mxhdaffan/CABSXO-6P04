text = str(input("Enter plaintext: "))
keys = [0, 1, 5]

for k in keys:
    print("\nKey: ", k)
    enc = ""
    for x in text:
        enc += chr(ord(x) ^ k)
    print("Encrypted Text = ", enc)
    
    dec = ""
    for y in enc:
        dec += chr(ord(y) ^ k)
    print("Decrypted Text = ", dec)