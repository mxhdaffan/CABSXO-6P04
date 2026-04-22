import numpy as np

key = np.array([[3,3],[2,5]])

inv_key = np.array([[15,17],[20,9]])

text = input("Enter plaintext: ").upper().replace(" ","")

nums = [ord(i) - 65 for i in text]

if len(nums) % 2 != 0:
    nums.append(23)   

cipher = []

for i in range(0, len(nums), 2):
    pair = np.array([[nums[i]], [nums[i+1]]])
    result = np.dot(key, pair) % 26
    cipher += [int(result[0][0]), int(result[1][0])]

cipher_text = "".join(chr(i + 65) for i in cipher)
print("Encrypted text:", cipher_text)

plain = []

for i in range(0, len(cipher), 2):
    pair = np.array([[cipher[i]], [cipher[i+1]]])
    result = np.dot(inv_key, pair) % 26
    plain += [int(result[0][0]), int(result[1][0])]

plain_text = "".join(chr(i + 65) for i in plain)
print("Decrypted text:", plain_text)