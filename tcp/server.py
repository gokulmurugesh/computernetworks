import socket

with socket.socket() as s:
    s.bind(('127.0.0.1',12345))
    s.listen()

    con, addr = s.accept()
    client_msg = con.recv(1024).decode()
    print('Message from client',client_msg)

    con.send('TCP'.encode())
    s.close()