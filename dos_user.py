import socket

s = socket.socket()
s.connect(('localhost',6000))

s.send(b'yes')
msg = s.recv(1024).decode()
print(msg)