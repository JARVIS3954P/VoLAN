import socket

s=socket.socket()

print("Socket Created")

s.bind(('192.168.101.12',9999))

s.listen(3)
print('Waiting for Incoming Connection')

while True:
    c, addr = s.accept()

    name = c.recv(1024).decode()
    print('Connected to' , addr, name)

    c.send(bytes('Welcome to VoLAN','utf-8'))

    c.close()



