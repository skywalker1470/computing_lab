# Requires: pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 1) generate keys
key = RSA.generate(2048)
private_pem = key.export_key()
public_pem  = key.publickey().export_key()

# 2) prepare message
message = b'Hello, public-key world!'

# 3) encrypt with PUBLIC key
pub = RSA.import_key(public_pem)
encryptor = PKCS1_OAEP.new(pub)
ciphertext = encryptor.encrypt(message)

# 4) decrypt with PRIVATE key
priv = RSA.import_key(private_pem)
decryptor = PKCS1_OAEP.new(priv)
plaintext = decryptor.decrypt(ciphertext)

print("Original:", message)
print("Encrypted (hex):", ciphertext.hex())
print("Decrypted:", plaintext)
