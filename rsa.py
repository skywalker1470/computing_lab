import random
def gcd(a,b):
    while b!=0:
        a,b = b , a%b
    return a
def prime_number_check(a):
    if a < 2:
        return False
    else:
        for i in range(2,a):
            if(a%i==0):
                return False
        return True

def gen_rand_prime():
    num = random.randint(100,400)
    while not prime_number_check(num):
        num = random.randint(100,400)
    return num

def modulo_inverse(num, m):
    ans=pow(num , -1 , m)
    return ans

p = gen_rand_prime()
q = gen_rand_prime()
while p==q:
    q = gen_rand_prime()

n = p*q
phi = (p-1)*(q-1)
e = 65537
while gcd(e,phi)!=1:
    e += 2

d = modulo_inverse(e,phi)

print(f"Public Key: ({e},{n})") 
print(f"Private Key: ({d},{n})")

plain_text = int(input(print("Give number : ")))

cipher = pow(plain_text , e , n)
print(f"Encrypted number: {cipher}")

decrypt = pow(cipher , d , n)
print(f"Decrypted number: {decrypt}")
