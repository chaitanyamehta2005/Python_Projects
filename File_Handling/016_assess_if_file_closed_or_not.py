
filename = r"C:\Users\Chaitanya\Documents\Hi.txt"
fileObj = open(filename)
print(fileObj.closed)
fileObj.close()
print(fileObj.closed)
