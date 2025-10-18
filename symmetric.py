# Shared symmetric key
key = "secret"

# XOR encryption/decryption function
def xor_crypt(message, key):
    result = ''
    for i, char in enumerate(message):
        # XOR each character's ASCII code with corresponding key character's ASCII code
        result += chr(ord(char) ^ ord(key[i % len(key)]))
    return result

# Original message to send
original_message = "Mid exams are from next Monday"

# Sender encrypts the message
encrypted_message = xor_crypt(original_message, key)

# Print encrypted message in hex to avoid garbled output
print("Encrypted message sent (hex):", encrypted_message.encode().hex())

# Receiver decrypts the message using the same key
decrypted_message = xor_crypt(encrypted_message, key)
print("Decrypted message received:", decrypted_message)
