p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = inverse_mod(e, phi)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

M = 31
print("\nOriginal Message:", M)

C = power_mod(M, e, n)
print("\nEncrypted Message:", C)

M_dec = power_mod(C, d, n)
print("Decrypted Message:", M_dec)