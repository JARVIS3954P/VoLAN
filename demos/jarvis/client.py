import socket

c = socket.socket()

c.connect(('192.168.101.12',9999))

name = input("Enter Your Name")
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())