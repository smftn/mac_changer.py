
#!/usr/bin/env python

import subprocess
import optparse

def input_values():
	reader = optparse.OptionParser()
	reader.add_option("-i", "--interface", dest = "interface", help = "Network Interface Name")
	reader.add_option("-m", "--mac", dest = "new_mac", help = "New MAC Address")
	(values, key) = reader.parse_args()

	if not values.interface:
		reader.error("[-] enter an interface name, --help") #error prompt to enter a network interface e.g. eth0/wlan0
	elif not values.new_mac:
		reader.error("[-] enter a new MAC address, --help") #error prompt to enter a mac/valid mac address formart 00:00:00:00:00:00
	return values

def change_mac(interface, new_mac):
	print ("changing the MAC address of the interface " + interface + " to " + new_mac)
	subprocess.call(["ifconfig", interface, "down"]) #brings the interface down
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac]) #changeing mac
	subprocess.call(["ifconfig", interface, "up"]) #brings up the network interface

values = input_values()
change_mac(values.interface, values.new_mac)
