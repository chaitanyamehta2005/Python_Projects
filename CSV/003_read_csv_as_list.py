import csv

def read_row(csv_filename):
    output_lst = []
    with open(csv_filename) as file:
        csv.data = csv.reader(file, delimiter=',')
        for row in csv.data:
            output_lst.append(row)
        return output_lst

print(read_row('data.csv'))
