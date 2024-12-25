import os

def get_arp_table():
    if os.name == 'nt':  # Windows
        arp_command = "arp -a"
    else:  # Linux/macOS
        arp_command = "arp -n"
    os.system(arp_command)

if __name__ == "__main__":
    get_arp_table()
