dict1 = {}

for i in range(0, 26):
    dict1[i] = chr(ord('a') + i)

#print(dict1)


def get_keys():


    for k1 in range(0, 100):
        for k2 in range (0, 100):

            if (((ord('a') - ord('a'))*k1 + k2 ) % 26 == (ord('G') - ord('A'))) and (((ord('b') - ord('a'))*k1 + k2 ) % 26 == (ord('L') - ord('A'))):
                print(f'k1: {k1}, k2: {k2}')
                return k1, k2

            


def decrypt(enc, k1, k2):
    plain = ""
    inv_key = pow(k1, -1, 26)

    for k in range(len(enc)):
        
            a = (((ord(enc[k]) - ord('A')) - k2) * inv_key) % 26
            plain += dict1[a]

    return plain

    


ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGFXANMGNVS"

k1, k2 = get_keys()

plaintext = decrypt(ciphertext, k1, k2)

print(f'ciphertext: {ciphertext}')

print(f'decrypted: {plaintext}')













