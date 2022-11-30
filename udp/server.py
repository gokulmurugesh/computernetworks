import socket

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:

    while True:
        s.sendto('UDP'.encode(), ('127.0.0.1',12345))