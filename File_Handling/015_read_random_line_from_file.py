import random
def read_random_lines(filename):
    with open(filename) as fileObj:
        data = fileObj.read().splitlines()
        return random.choice(data)

filename = r"C:\Users\Chaitanya\Documents\Hi.txt"
print(read_random_lines(filename))