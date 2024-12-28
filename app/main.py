'''
Right now program just setups a TCP connection between two devices (PTP connection) connected on lan in our case we talk to our own device,
but it will also list the router(moblie hotspot)
Usage is as follows....
1. Run the script and select the server option first
2. Once the server starts listening run the Client
3. Client lists your IP and all the other avalable IP on the network
4. Choose your device's IP and type the message for Server
5. For closing the connection type "close" and send to server

This script will also work on two different devices in the same local network if they both run this same python script
'''

import logging
import os
import core.networking as nt
import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')

class MyFirstKivyAPP(App):
    def build(self):
        lbl = Label(text="Hello World")
        return lbl


os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    app = MyFirstKivyAPP()
    app.run()

    #print("READ THE PYTHON FILE FIRST BEFORE USING!!!")
    #option = int(input("1. Sender (Client)\n2. Reciver (Server)\nEnter you choice: "))
    #if option == 1:
    #    nt.run_client()
    #elif option == 2:
    #    nt.run_server()
    #else:
    #    print("INVALID OPTION TERMINATING..")
