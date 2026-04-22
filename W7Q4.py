P = int(input("Enter a prime number: "))
G = int(input("Enter primitive root: "))

a = int(input("\nEnter private key of Alice: "))
b = int(input("Enter private key of Bob: "))

x = (G**a) % P
y = (G**b) % P

print("\nAlice generated public key: ", x)
print("Bob generated public key: ", y)

ka = (y**a) % P
kb = (x**b) % P

print("\nSecret key of Alice: ", ka)
print("Secret key of Bob: ", kb)