#!/usr/bin/env python3

import subprocess
import random
import optparse
import re


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter the interface to change the MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify the interface, use --help for more info")
    return options


def generate_random_mac():
    # Fix the first three bytes (00:74:77)
    mac = [
        0x00,  # first byte
        0x74,  # second byte
        0x77,  # third byte
        random.randint(0x00, 0xFF),  # fourth byte
        random.randint(0x00, 0xFF),  # fifth byte
        random.randint(0x00, 0xFF)  # sixth byte
    ]
    return ':'.join(f"{byte:02x}" for byte in mac)


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("No MAC address found.")
            return None
    except subprocess.CalledProcessError:
        print(f"Could not read MAC address for {interface}.")
        return None


# Main logic
options = get_argument()
interface = options.interface
new_mac = generate_random_mac()

# Print the current MAC address
current_mac = get_current_mac(interface)
if current_mac:
    print(f"[+] Current MAC address: {current_mac}")

# Change the MAC address
change_mac(interface, new_mac)

# Verify the MAC has been changed
updated_mac = get_current_mac(interface)
if updated_mac == new_mac:
    print(f"[+] MAC address successfully changed to {updated_mac}")
else:
    print(f"[-] Failed to change MAC address. Current MAC is still {updated_mac}")
