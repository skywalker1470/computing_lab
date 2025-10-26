import socket
s = socket.socket()
s.bind(('localhost', 6000))
s.listen(5)
print("Listening....")
count = 0 
while True:
    try:
        connection , addr = s.accept()
        print(f"Connected to {addr}")
        msg = connection.recv(1024).decode()
        if(msg != 'yes'):
            count += 1
        if count > 3:
            connection.send(b"DOS Attack")
        else:
             connection.send(b"Message Recieved")
        connection.close()
    except:
        pass             