sabotage = """
sum = 0 
for i in range(3,21):
    sum+=i
print(sum)
"""
with open('easy.py', 'r') as file:
    code = file.read()
print(f"The original code is : {code}")
with open('easy.py', 'w') as file:
    file.write(sabotage)
print("The file has been sabotaged")
exec(open('easy.py').read())