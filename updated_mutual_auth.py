import hashlib
import secrets

shared_secret = "mutualkey"

def generate_challenge():
  
    return secrets.token_hex(16)

def create_response(challenge, secret):
    
    response = hashlib.sha256((challenge + secret).encode()).hexdigest()
    return response

def verify_response(challenge, secret, response):
    
    expected = hashlib.sha256((challenge + secret).encode()).hexdigest()
    return response == expected

def alice_challenge():
    challenge = generate_challenge()
    print(f"Alice's challenge: {challenge}")
    return challenge

def bob_response(challenge):
    response = create_response(challenge, shared_secret)
    print(f"Bob's response: {response}")
    return response

def alice_verify(response, challenge):
    if verify_response(challenge, shared_secret, response):
        print("Alice trusts Bob")
    else:
        print("Trust failed")

def bob_challenge():
    challenge = generate_challenge()
    print(f"Bob's challenge: {challenge}")
    return challenge

def alice_response(challenge):
    response = create_response(challenge, shared_secret)
    print(f"Alice's response: {response}")
    return response

def bob_verify(response, challenge):
    if verify_response(challenge, shared_secret, response):
        print("Bob trusts Alice")
    else:
        print("Trust failed")

challenge = alice_challenge()
response = bob_response(challenge)
alice_verify(response, challenge)

challenge = bob_challenge()
response = alice_response(challenge)
bob_verify(response, challenge)
