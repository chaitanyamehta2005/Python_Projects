import csv

def read_row(csv_filename):
    with open(csv_filename) as file:
        csv.data = csv.reader(file, delimiter=',')
        for row in csv.data:
            print(', '.join(row))

read_row('data.csv')
