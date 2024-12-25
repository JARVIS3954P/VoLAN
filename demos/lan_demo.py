
from scapy.all import ARP, Ether, srp
import socket
import sys

def get_local_ip():
    """Get the local IP address of the machine."""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        print(f"Error fetching local IP: {e}")
        sys.exit(1)

def scan_network(ip_range):
    """Scan the network for devices."""
    # Create an ARP request packet
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Send the packet and capture the response
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in answered_list:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def main():
    print("Scanning the network...")
    local_ip = get_local_ip()
    ip_range = ".".join(local_ip.split('.')[:3]) + ".1/24"
    print(f"IP range: {ip_range}")
    devices = scan_network(ip_range)

    if devices:
        print(f"Found {len(devices)} devices on the network:")
        for idx, device in enumerate(devices, start=1):
            print(f"{idx}. IP: {device['ip']} - MAC: {device['mac']}")
    else:
        print("No devices found on the network.")

if __name__ == "__main__":
    main()
