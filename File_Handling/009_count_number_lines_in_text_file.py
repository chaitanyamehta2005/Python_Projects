def count_lines(filename):
    count = 0
    with open(filename,'r') as fileObj:
        while True:
            data = fileObj.readline()
            if data =='':
                break
            else:
                count+=1
    return count


filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
total_lines = count_lines(filename)
print("There are total {0} line(s) in the file".format(total_lines))