dict1 = {}

alphabets = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabets)):
    dict1[i] = alphabets[i]

print(dict1)

def encrypt(s, key):
    enc = ""
    for j in range(len(s)):
        if s[j] == " ":
            continue

        elif s[j].isupper():
            a = ((ord(s[j]) - ord('A')) + key) % 26
            enc += dict1[a].upper()

        else:
            a = ((ord(s[j]) - ord('a')) + key) % 26
            enc += dict1[a]

    return enc


def decrypt(enc, key):
    plain = ""
    for k in range(len(enc)):
        if enc[k].isupper():
            a = ((ord(enc[k]) - ord('A')) - key) % 26
            plain += dict1[a].upper()

        else:
            a = ((ord(enc[k]) - ord('a')) - key) % 26
            plain += dict1[a]

    return plain


text = "I am learning information security"
k = 20

ciphertext = encrypt(text, k)

plaintext = decrypt(ciphertext, k)

print(f'original: {text}')
print(f'encrypted: {ciphertext}')
print(f'decrypted: {plaintext}')
