import socket
import sys
from scapy.all import ARP, Ether, srp
import logging
import os

# Ensure the logs/ folder exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    handlers=[
        logging.FileHandler("logs/app.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)
def get_local_ip():
    """Get the local IP address of the machine."""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        logging.info(f"Hostname: {hostname}")
        logging.info(f"Local IP: {local_ip}")
        return local_ip
    except Exception as e:
        logging.error(f"Error fetching local IP: {e}")
        sys.exit(1)


def find_devices_on_lan():
    local_ip = get_local_ip()


# Example usage
if __name__ == "__main__":
    find_devices_on_lan();
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")
