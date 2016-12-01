import socket

sock = socket.socket()
sock.bind(('127.0.0.2', 9090))
sock.listen(1)
while True:
    conn, addr = sock.accept()

    print ('connected:', addr)

    while True:
        data = conn.recv(1024)
        if not data:
           break
        import random
        ID=random.randrange(100000)
        import hashlib
        ID = hashlib.md5()
        print(ID.digest())
        conn.send(ID.digest())

    conn.close()