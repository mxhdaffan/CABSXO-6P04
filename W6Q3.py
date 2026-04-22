def generate_matrix(key):
    key = key.upper().replace("J","I")
    matrix = []
    used = []

    for i in key: 
        if i not in used and i.isalpha():
            used.append(i)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for i in alphabet:
        if i not in used:
            used.append(i)

    for i in range(0,25,5):
        matrix.append(used[i:i+5])

    return matrix


def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i,j


def prepare_text(text):
    text = text.upper().replace("J","I")
    text = text.replace(" ","")
    pairs = []

    i = 0
    while i < len(text):
        a = text[i]
        if i+1 < len(text):
            b = text[i+1]
            if a == b:
                pairs.append(a + "X")
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + "X")
            i += 1
    return pairs


def encrypt(matrix, pairs):
    cipher = ""

    for pair in pairs:
        r1,c1 = find_position(matrix, pair[0])
        r2,c2 = find_position(matrix, pair[1])

        if r1 == r2:
            cipher += matrix[r1][(c1+1)%5]
            cipher += matrix[r2][(c2+1)%5]

        elif c1 == c2:
            cipher += matrix[(r1+1)%5][c1]
            cipher += matrix[(r2+1)%5][c2]

        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


def decrypt(matrix, text):
    plain = ""

    for i in range(0,len(text),2):
        a = text[i]
        b = text[i+1]

        r1,c1 = find_position(matrix,a)
        r2,c2 = find_position(matrix,b)

        if r1 == r2:
            plain += matrix[r1][(c1-1)%5]
            plain += matrix[r2][(c2-1)%5]

        elif c1 == c2:
            plain += matrix[(r1-1)%5][c1]
            plain += matrix[(r2-1)%5][c2]

        else:
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain


key = input("Enter key: ")
text = input("Enter plaintext: ")

matrix = generate_matrix(key)

print("\nKey Matrix:")
for row in matrix:
    print(row)

pairs = prepare_text(text)

cipher = encrypt(matrix, pairs)
print("\nEncrypted Text:", cipher)

decrypted = decrypt(matrix, cipher)
print("Decrypted Text:", decrypted)