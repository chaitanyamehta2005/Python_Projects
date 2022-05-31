def read_all_lines(filename):
    with open(filename, 'r') as fileObj:
        data = ''
        for line in fileObj:
            data = data+line
        return data


filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
output = read_all_lines(filename)
print("The {0} variable after reading all the lines of file is : \n{1}".format(type(output),output))