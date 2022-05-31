def find_longest_word(filename):
    with open(filename, 'r') as fileObj:
              words = fileObj.read().split()
    max_len = len(max(words, key=len))
    return [i for i in words if len(i) == max_len]


filename = r"C:\Users\Chaitanya\Documents\Hello.txt"
output = find_longest_word(filename)
print(output)
