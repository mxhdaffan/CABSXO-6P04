p = 17
E = EllipticCurve(GF(p), [2, 2])

# Base point (generator)
G = E(5, 1)
n = G.order()

print("Elliptic Curve:", E)
print("Base Point G:", G)

a = randint(1, n-1)   # private key of Alice
b = randint(1, n-1)   # private key of Bob

A = a * G             # public key of ALice
B = b * G             # public key of Bob

print("\nAlice's Private Key:", a)
print("Bob's Private Key:", b)

print("\nAlice's Public Key:", A)
print("Bob's Public Key:", B)

# Alice sends A (public key) to Bob
# Bob sends B (public key) to Alice
ka = a * B
kb = b * A

print("\nShared Secret computed by Alice:", ka)
print("Shared Secret computed by Bob:", kb)

print("\nKeys match?", ka == kb)