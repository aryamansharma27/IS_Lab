dict1 = {}

for i in range(26):
    dict1[i] = chr(ord('a') + i)

#print(dict1)


def encrypt(s, key):
    enc = ""
    for j in range(len(s)):
        if s[j] == " ":
            continue

        elif s[j].isupper():
            a = ((ord(s[j]) - ord('A')) * key) % 26
            enc += dict1[a].upper()

        else:
            a = ((ord(s[j]) - ord('a')) * key) % 26
            enc += dict1[a]

    return enc

def decrypt(enc, key):
    plain = ""

    inv_key = pow(key, -1, 26)
    for k in range(len(enc)):
        if enc[k].isupper():
            a = ((ord(enc[k]) - ord('A')) * inv_key) % 26
            plain += dict1[a].upper()

        else:
            a = ((ord(enc[k]) - ord('a')) * inv_key) % 26
            plain += dict1[a]

    return plain


text = "I am learning information security"
k = 15

print(f'original: {text}')

ciphertext = encrypt(text, k)

plaintext = decrypt(ciphertext, k)

print(f'encrypted: {ciphertext}')

print(f'decrypted: {plaintext}')
