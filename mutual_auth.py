shared_secret = "mutualkey"
def alice_challenge():
    challenge = 'Alice challenge'
    print(f"Alice's challenge : {challenge}")
    return challenge
def bob_response(challenge):
    response = challenge + shared_secret
    print(f"Bob's response : {response}")
    return response
def alice_verify(response , challenge):
    expected = challenge + shared_secret
    if(response == expected):
        print("Alice trusts bob")
    else:
        print("trust failed")

def bob_challenge():
    challenge = 'Bob challenge'
    print(f"Bob's challenge : {challenge}")
    return challenge
def alice_response(challenge):
    response = challenge + shared_secret
    print(f"Alice's response : {response}")
    return response
def bob_verify(response , challenge):
    expected = challenge + shared_secret
    if(response == expected):
        print("Bob trusts Alice")
    else:
        print("trust failed")
        
challenge = alice_challenge()
response = bob_response(challenge)
alice_verify(response , challenge)
challenge = bob_challenge()
response = alice_response(challenge)
bob_verify(response,challenge)
