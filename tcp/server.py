import socket

with socket.socket() as s:
    s.bind((socket.gethostname(),12345))
    s.listen()

    con, addr = s.accept()
    con.send('TCP'.encode())

    s.close()