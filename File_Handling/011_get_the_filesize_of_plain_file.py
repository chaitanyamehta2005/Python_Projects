import os
def file_size(filename):
    statinfo = os.stat(filename)
    return  statinfo.st_size


filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
size = file_size(filename)
print("The file size is {0}".format(size))
