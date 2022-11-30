import socket

with socket.socket() as s:
    s.connect((socket.gethostname(),12345))

    print(s.recv(1024).decode())

    s.close()