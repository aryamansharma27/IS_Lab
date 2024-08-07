dict1 = {}


for i in range(26):
    dict1[i] = chr(ord('a') + i)

#print(dict1)

def encrypt(s, keyword):
    key = ""

    for j in range(len(s)):
        key += keyword[j % len(keyword)]

    print(key)

    cipher = ""

    for k in range(len(s)):

        if s[k].isupper():
            a = ((ord(key[k]) - ord('a')) + (ord(s[k]) - ord('A'))) % 26
            cipher += dict1[a].upper()

        else:
            a = ((ord(key[k]) - ord('a')) + (ord(s[k]) - ord('a'))) % 26
            cipher += dict1[a]

    return cipher, key


def decrypt(ciphertext, keyword):

    key = ""

    for i in range(len(ciphertext)):

        key += keyword[i % len(keyword)]

    plain = ""

    for j in range(len(ciphertext)):

        if ciphertext[j].isupper():
            a = ((ord(ciphertext[j]) - ord('A')) - (ord(key[j]) - ord('a'))) % 26
            plain += dict1[a].upper()
                
            
        
        else:
            a = ((ord(ciphertext[j]) - ord('a')) - (ord(key[j]) - ord('a'))) % 26 
            plain += dict1[a]
            
    return plain
    
    

    


text = "jattdamuqabla"

keyword = "gang"



ciphertext, key = encrypt(text, keyword)

plaintext = decrypt(ciphertext, keyword) 

print(f'original: {text}')
print(f'encrypted: {ciphertext}')
print(f'decrypted: {plaintext}')

