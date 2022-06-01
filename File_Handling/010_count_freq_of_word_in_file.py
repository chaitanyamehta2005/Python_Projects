def count_lines(filename,word):
    count = 0
    with open(filename,'r') as fileObj:
        while True:
            data = fileObj.readline()
            if data =='':
                break
            else:
                data_lst =list(data.split())
                count = count +(data_lst.count(word))
    return count


filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
word = input("Enter the word for which you want to get frequency: ")
word_freq = count_lines(filename,word)
print("Frequency of word {0} in file is {1}".format(word,word_freq))