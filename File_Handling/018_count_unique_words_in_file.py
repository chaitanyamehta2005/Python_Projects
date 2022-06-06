def count_unique_words(filename):
    with open(filename) as fileObj:
        data = fileObj.read()
        data.replace(',',' ')
        data.split(' ')
        return len(data)


filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
print(count_unique_words(filename))
