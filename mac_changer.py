#!/usr/bin/env python3

import subprocess
import random
import optparse

# Set up command line options
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Enter the interface to change the MAC address")
(options, arguments) = parser.parse_args()

# Check if the interface option was provided
if not options.interface:
    print("[-] Please specify an interface using -i option.")
    exit(1)

def generate_random_mac():
    # Fix the first three bytes (00:74:77)
    mac = [
        0x00,  # first byte
        0x74,  # second byte
        0x77,  # third byte
        random.randint(0x00, 0xFF),  # fourth byte
        random.randint(0x00, 0xFF),  # fifth byte
        random.randint(0x00, 0xFF)   # sixth byte
    ]
    return ':'.join(f"{byte:02x}" for byte in mac)
def change_mac(interface,new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

new_mac = generate_random_mac()
interface = options.interface

change_mac(interface,new_mac)
print(f"[+] Changing MAC address for {interface}")



# Change the MAC address


print(f"[+] Your {interface} MAC address has been changed to {new_mac}")
