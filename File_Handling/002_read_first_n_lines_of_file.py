def read_nlines(filename, n):
    """ This function will read first n lines of the file"""
    fileObj = open(filename, 'r')
    for i in range(n):
        print(fileObj.readline())


filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
read_nlines(filename, 4)
