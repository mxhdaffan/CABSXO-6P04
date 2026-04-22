p = 17
E = EllipticCurve(GF(p), [2, 2])            # y^2 = x^3 + ax + b

# Base point
G = E(5, 1)
n = G.order()       # number of times you can add G to itself before cycling

# Key Generation
d = randint(1, n-1)   # Private key
Q = d * G             # Public key

print("Private Key (d):", d)
print("Public Key (Q = d*G):", Q)

# Message (must be a point on curve)
M = E(6, 3)
print("\nOriginal Message (Point):", M)

# Encryption
k = randint(1, n-1)

C1 = k * G
C2 = M + k * Q

print("\nEncrypted Message:")
print("C1 =", C1)
print("C2 =", C2)

# Decryption
M_dec = C2 - d * C1

print("\nDecrypted Message:", M_dec)