def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def affine_decrypt(cipher, key):
    a, b = key
    a_inv = modinv(a, 26)
    if a_inv is None:
        return None
    return ''.join([chr(((a_inv * (ord(c) - ord('A') - b)) % 26) + ord('A')) for c in cipher])

ciphertext = "FAJSRWOXLAXDQZAWNDDVLSU"
valid_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

for a in valid_a:
    for b in range(26):
        key = [a, b]
        plaintext = affine_decrypt(ciphertext, key)
        if plaintext and 'FUN' in plaintext:
            print(f"[+] Key: {key} => {plaintext}")
