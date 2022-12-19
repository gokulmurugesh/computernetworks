import socket

with socket.socket() as s:
    s.connect(('127.0.0.1',12345))

    s.send('client-msg'.encode())
    
    print('Message from the server',s.recv(1024).decode())

    s.close()