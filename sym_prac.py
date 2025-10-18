key = 'secret'

message = 'Mid exams are from next Monday'

def xor_encrypt(message,key):
    cipher = ''
    for i , char in enumerate(message):
        cipher += chr(ord(char) ^ ord(key[i % len(key)]))
    return cipher

cipher = xor_encrypt(message,key)
print("Enctypted : ",cipher.encode().hex())
decipher = xor_encrypt(cipher,key)
print("Decrypted : ",decipher)  
    