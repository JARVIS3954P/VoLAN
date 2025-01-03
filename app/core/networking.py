import socket
import sys
import os 
import platform
from concurrent.futures import ThreadPoolExecutor


def get_local_ip():     #Fetches local IP address of the system (wlan0) not loopbackip
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('1.24.4.25',1)) 
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.1.1'
    finally:
        s.close()
    return IP


def run_server():   #Creates a TCP configured PTP server for incomming connections and listnes on port  by default
    print("Server Running......")
    ip = get_local_ip()
    port = 8000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(0)
    print(f"TCP Listening on port: {port}")
    client, client_add = server.accept()
    
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind((ip,0))
    udp_port = udp_server.getsockname()[1]
    
    client.send(str(udp_port).encode('utf-8'))
    client.close()
    server.close()
    print("TCP Connection closed")
    while True:
        data, addr = udp_server.recvfrom(1024)
        if(data.decode('utf-8').lower() == "close"): 
            udp_server.close() 
            print("UDP SERVER CLOSED!!!!")
            break
        print(f"Recived: {data.decode('utf-8')}")

def ping_ip(ip): #Pings the said IP address
    param = "-n" if platform.system().lower() == "windows" else "-c" 
    command = f"ping {param} 1 {ip} > /dev/null 2>&1"
    response = os.system(command)
    return ip if response == 0 else None

def scan_devices(base_ip):  #Returns the Devices avalable on the network(pingable devices)
    print("Scanning for devices.....")
    avalable_devices = []
    ips = [f"{base_ip}.{i}" for i in range(1,255)]
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(ping_ip,ips))
    avalable_devices = [ip for ip in results if ip]
    print("Found Devices: ")
    for count, device in enumerate(avalable_devices, 1):
        print(f"{count}.{device}")
    return avalable_devices

def get_device():   #Takes choise from the user for the device to connect to 
    local_ip = get_local_ip()
    print(f"Your IP on the local network is: {local_ip}")
    base_ip = '.'.join(local_ip.split('.')[:-1])
    devices_on_network = scan_devices(base_ip)
    device_to_connect = int(input("Enter device to connect to: "))
    return devices_on_network[device_to_connect-1]



def run_client():       # Runs Client for the created TCP configured PTP server
    print("Client is running......") 
    server_add = get_device()
    server_port = 8000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_add,server_port))
    udp_server_port = client.recv(1024).decode('utf-8')
    client.close()
    print("TCP Connection Closed")
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        msg = input("Enter the message for the server: ")
        if msg == "close":
            client.close()
            break
        client.sendto(msg.encode('utf-8'),(server_add,int(udp_server_port)))
