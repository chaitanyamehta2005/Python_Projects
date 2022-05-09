import socket
import threading
import time
import socket

host = input("Enter the host ip address or domainname: ")

def port_scanner(host,port):
    socketObject = socket.socket()
    try:
        connection =socketObject.connect((host, port))
        print('port {0} is open'.format(port))
        connection.close()
    except:
        #print('port {0} is closed'.format(port))
        pass

for x in range(1,65535):
    t = threading.Thread(target = port_scanner, args=(host,x))
    t.start()


