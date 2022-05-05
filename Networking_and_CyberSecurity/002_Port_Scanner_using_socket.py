import socket

host = input("Enter the host ip address or domainname: ")
for port in range(1,65535):
    # creating the socket object
    socketObject= socket.socket()

    result =socketObject.connect_ex((host,port))

    if result ==0:
        print("Port {0} is open".format(port))
    else:
        print("Port {0} is NOT open".format(port))
    # destructing the socket object
    socketObject.close()