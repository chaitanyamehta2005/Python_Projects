# Precondition: Please make sure both the files have the same number of lines so that zip function can be used efficiently.

def combine_lines_from_two_files(file1,file2):
    with open(file1,'r')as fileObj1:
        with open(file2, 'r') as fileObj2:
            for a,b in zip(fileObj1,fileObj2):
                print(a + b)


file1 = r"C:\Users\Chaitanya\Documents\Hello.txt"
file2 = r"C:\Users\Chaitanya\Documents\Hi.txt"

combine_lines_from_two_files(file1,file2)