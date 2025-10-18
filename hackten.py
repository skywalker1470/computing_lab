code = """
sum = 0
for i in range(3,21):
    sum += i
print(sum)
"""
with open("onetoten.py", "r") as file:
    content = file.read()
    print("File content:\n", content)
print("Hacking now--")
with open("onetoten.py", "w") as file:
    file.write(code)
print("File hacked successfully.")
exec(open("onetoten.py").read())