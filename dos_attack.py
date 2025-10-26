import socket
while True:
    try:
        s = socket.socket()
        s.connect(('localhost',6000))
        s.send(b'Attack!!!')
    except:
        pass