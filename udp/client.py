import socket

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:    
    s.sendto('client-msg'.encode(),('127.0.0.1',12345))
    
    print('Message from the server',s.recv(1024).decode())
    
    s.close()