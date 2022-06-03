
def remove_newline(filename):
    fileObj= open(filename,'r')
    data = fileObj.readlines()
    return [s.rstrip('\n') for s in data]


filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
print(remove_newline(filename))