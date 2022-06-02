def write_list_to_file(filename,lst):
    with open(filename,'w') as fileObj:
        for elem in lst:
            fileObj.write(elem+'\n')

filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
orig_lst =  ['red','green','blue','orange']
write_list_to_file(filename,orig_lst)

