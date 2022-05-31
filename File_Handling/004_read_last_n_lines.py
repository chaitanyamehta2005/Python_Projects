def read_last_n_lines(filename, n):
    with open(filename, 'r') as fileObj:
        data = list(fileObj.readlines())
        try:
            for i in range(-n, 0, 1):
                print(data[i], end='')
        except IndexError:
            print("Error: File does not have the number of lines as per your input")


filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
read_last_n_lines(filename, 15)
