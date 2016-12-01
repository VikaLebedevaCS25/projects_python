import socket

sock = socket.socket()
sock.connect(('127.0.0.2', 9090))
ID=0
if ID==0:
    sock.send("Name Me".encode())

    ID = sock.recv(1024)
    sock.close()

    print (ID)
else:
	sock.send(ID)
	sock.close()

	print (ID)