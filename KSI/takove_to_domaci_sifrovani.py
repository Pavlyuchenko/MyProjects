import math

def encode(n, plain_text): # vraci ciphertext typu String
    res = ""

    for i in range(1, math.ceil(len(plain_text) / n)+1):
        res += plain_text[i*n-n:i*n][::-1]

    return res


def decode(n, cipher_text): # vraci plaintext typu String
    res = ""

    for i in range(1, math.ceil(len(cipher_text) / n)+1):
        res += cipher_text[i*n-n:i*n][::-1]

    return res

# Testy:
print(encode(3, "Ahoj")) # ohAj
print(encode(2, "Ahoj")) # hAjoyk
print(encode(3, "12345")) # 32154
print(decode(2, "hAjo")) # Ahoj
print(decode(3, encode(3, "Karlik a Los Karlos komunikuji sifrovane"))) # Karlik a Los Karlos komunikuji sifrovane

# na automaticke testy doporucuji assert
