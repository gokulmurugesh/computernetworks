import socket

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1',12345))

    data, addr = s.recvfrom(1024)
    print('Message from the client',data.decode())
    
    s.sendto('UDP'.encode(), addr)
