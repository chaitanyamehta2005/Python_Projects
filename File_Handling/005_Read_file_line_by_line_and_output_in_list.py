def read_all_lines(filename):
    with open(filename, 'r') as fileObj:
        data = fileObj.readlines()
        return data


filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
output = read_all_lines(filename)
print("The list created after reading all the lines of file is : \n{0}".format(output))