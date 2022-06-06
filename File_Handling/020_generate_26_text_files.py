def generate_files():
    for i in range(65, 91):
        filename = chr(i) + '.txt'
        with open(filename, 'x') as f:
            f.close()


generate_files()
