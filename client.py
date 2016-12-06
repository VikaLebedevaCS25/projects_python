import	socket

sock=	socket.socket()
sock.connect(('127.0.0.2', 9090))
f	=	open('d:\\ID.txt','w+')
ID	=	f.read()
if	not	ID:
	sock.send("Name Me".encode())
	ID	=	sock.recv(1024)
	f.write(str(ID)	+	'\n')
	f.close()
	sock.close()

	print(ID)
	
else:
	sock.send(ID)
	sock.close()
	
	print(ID)
