dict1 = {}

alphabets = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabets)):
    dict1[i] = alphabets[i]


def encrypt(plain, key):

    cipher = ""

    no_spaces = ""

    for i in range(len(plain)):
        if plain[i] != " ":
            no_spaces += plain[i] 

    for i in range(len(no_spaces)):

        if i == 0:
                keyvalue = key

        else:
            keyvalue = ord(no_spaces[i-1]) - ord('a')
        
        new_val = (ord(no_spaces[i]) - ord('a') + keyvalue) % 26

        cipher += dict1[new_val]

    
    print(f'encrypted: {cipher}')

    return cipher




def decrypt(cipher, plaintext, key):

    no_spaces = ""

    for i in range(len(plaintext)):

        if plaintext[i] != " ":
            no_spaces += plaintext[i]


    plain = ""

    
    for i in range(len(cipher)):
        if i == 0:
            key_val = key

        else:
            key_val = ord(no_spaces[i-1]) - ord('a')
        
        new_val = (ord(cipher[i]) - ord('a') - key_val) % 26

        plain += dict1[new_val]

    print(f'decrypted: {plain}')

    return plain

   


plaintext = "the house is being sold tonight"

key = 10


ciphertext = encrypt(plaintext, key)

decrypted = decrypt(ciphertext, plaintext, key)


