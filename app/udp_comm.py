import socket

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

def server():
    print("Server has started...")
    ip = get_local_ip()
    port = 8000
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.bind((ip,port))
    while True:
        data, addr = server.recvfrom(1024)
        if data.decode('utf-8').lower() == "close":
            server.close()
            break
        print(f"Recieved:{data.decode("utf-8")}")

def client():
    print("Client has started...")
    ip = get_local_ip()
    port = 8000
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        msg = input("Enter the msg for server: ")
        client.sendto(msg.encode('utf-8'), (ip,port))

if __name__ == "__main__":
    print("1. Server")
    print("2. Client")
    option = int(input("Enter your choice: "))
    if option == 1:
        server()
    elif option == 2:
        client()
    else:
        print("Invalid Option")

