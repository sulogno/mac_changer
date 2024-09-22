# MAC Address Changer

A simple Python script to randomly generate a MAC address and change the MAC address of a specified network interface on Linux systems.

## Features

- **Generate Random MAC**: The script generates a random MAC address with the first three octets fixed (`00:74:77`), and the last three randomly generated.
- **Change MAC Address**: It allows you to change the MAC address of any network interface on a Linux system.
- **Verify Change**: After changing the MAC address, the script verifies if the change was successful.

## Requirements

- Python 3.x
- `ifconfig` command available (part of `net-tools` package on Linux)
- Root privileges (required to change MAC address)

## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/mac-address-changer.git
   cd mac-address-changer
## Run the script with root privileges:

```bash
sudo python3 mac_changer.py -i <interface>
```
Replace <interface> with the name of the network interface for which you want to change the MAC address (e.g., eth0, wlan0, etc.).

## Example:
```bash
sudo python3 mac_changer.py -i eth0
```
## How It Works
1. The script takes the network interface as input using the -i option.
2. It generates a random MAC address with the first three bytes fixed and the last three bytes randomized.
3. The script uses the ifconfig command to bring the network interface down, change the MAC address, and then bring the interface back up.
4. It then prints the old and new MAC addresses and verifies if the change was successful.
## Code Explanation
1. get_argument(): Parses the command-line arguments to get the network interface.
2. generate_random_mac(): Generates a random MAC address with a fixed prefix (00:74:77) and random suffix.
3. change_mac(): Uses the ifconfig command to change the MAC address of the specified interface.
4. get_current_mac(): Uses ifconfig to retrieve and return the current MAC address of the specified interface.
## Example Output
```bash
[+] Current MAC address: 00:74:77:92:3c:5b
[+] Changing MAC address for eth0 to 00:74:77:3e:5d:7f
[+] MAC address successfully changed to 00:74:77:3e:5d:7f
```
## License
1. This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements.

# Disclaimer
Changing your MAC address might cause network disruptions or violations of your network's policies. Please make sure to use this tool responsibly and only on networks where you have permission to modify MAC addresses.

## Additional Steps:
Replace the URL in the "Clone the repository" section with the actual link to your GitHub repository.
Optionally, you can add more sections like Known Issues or FAQ based on user feedback or usage patterns.


