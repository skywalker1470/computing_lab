import random
def is_prime(num):
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True
def gen_prime():
    while True:
        num = random.randint(10,50)
        if is_prime(num):
            return num
def gcd(a,b):
    while b!=0:
        a,b = b, a % b
    return a
def modinv(a,m):
    for x in range(1,m):
        if(a*x) % m  ==1:
            return x

p = gen_prime()
q = gen_prime()
while p == q:
    q = gen_prime()
    
n = p * q
phi = (p-1)*(q-1)

e = 65573
while gcd(e,phi) != 1:
    e += 2

d = modinv(e,phi)
print("Public Key: (e={}, n={})".format(e,n))
print("Private Key: (d={}, n={})".format(d,n))
    
def encrypt_rsa(message,e,n):
    cipher = []
    for char in message:
        m = ord(char)
        c = pow(m,e,n)
        cipher.append(c)
    return cipher
def decrypt_rsa(cipher,d,n):
    message = ''
    for c in cipher:
        m = pow(c,d,n)
        message += chr(m)
    return message
# Example usage
original_message = "Mid exams are from next Monday"                 
    
ciphertext = encrypt_rsa(original_message,e,n)
print("Encrypted message (ciphertext):", ciphertext)
decrypted_message = decrypt_rsa(ciphertext,d,n)
print("Decrypted message:", decrypted_message)
      