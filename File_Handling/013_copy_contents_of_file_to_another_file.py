def write_list_to_file(from_file,to_file):
    with open(from_file,'r') as readfileObj:
        with open(to_file,'w') as writefileObj:
            writefileObj.write(readfileObj.read())

from_filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
to_filename = r"C:\Users\Chaitanya\Documents\destination.txt"

write_list_to_file(from_filename,to_filename)
