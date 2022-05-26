
fileObj = open(r"C:\Users\Chaitanya\Documents\Hello.txt")
print(fileObj.read())
fileObj.close()

print("\n")

fileObj = open(r"C:\Users\Chaitanya\Documents\Hello.txt")
for line in fileObj:
    print(line,end='')
fileObj.close()
