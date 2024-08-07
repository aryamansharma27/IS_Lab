dict1 = {}

alphabets = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabets)):
    dict1[i] = alphabets[i]

#print(dict1)


def encrypt(s, k1, k2):
    enc = ""

    for j in range(len(s)):
        if s[j] == " ":
            continue

        elif s[j].isupper():
            a = (((ord(s[j]) - ord('A')) * k1) + k2) % 26
            enc += dict1[a].upper()

        else:
            a = (((ord(s[j]) - ord('a')) * k1) + k2) % 26
            enc += dict1[a]

    return enc


def decrypt(enc, k1, k2):
    plain = ""
    inv_key = pow(k1, -1, 26)

    for k in range(len(enc)):
        if enc[k].isupper():
            a = (((ord(enc[k]) - ord('A')) - k2) * inv_key) % 26
            plain += dict1[a].upper()

        else:
            a = (((ord(enc[k]) - ord('a')) - k2) * inv_key) % 26
            plain += dict1[a]

    return plain


text = "I am learning information security"

key1 = 15
key2 = 20

ciphertext = encrypt(text, key1, key2)

plaintext = decrypt(ciphertext, key1, key2)

print(f'original: {text}')
print(f'encrypted: {ciphertext}')
print(f'decrypted: {plaintext}')
