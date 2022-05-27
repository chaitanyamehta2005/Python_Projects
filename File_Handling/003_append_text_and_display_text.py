filepath = r"..\..\..\Hello1.txt"
fileObj = open(filepath,'a')
fileObj.write(input("Please enter text you want to append to the file: "))
fileObj.close()
fileObj = open(filepath,'r')
print(fileObj.read())
fileObj.close()