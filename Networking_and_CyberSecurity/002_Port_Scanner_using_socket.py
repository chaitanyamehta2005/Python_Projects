import socket

# creating the socket object
host = input("Enter the host ip address or domainname: ")
for port in range(1,65535):
    socketObject= socket.socket()

    result =socketObject.connect_ex((host,port))

    if result ==0:
        print("Port {0} is open".format(port))
    else:
        print("Port {0} is NOT open".format(port))

    socketObject.close()