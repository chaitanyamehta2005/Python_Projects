import csv

def read_row(csv_filename):
    with open(csv_filename) as file:
        csv.data = csv.reader(file, delimiter='\t')
        for row in csv.data:
            print('\t '.join(row))

read_row('tab_separated_data.csv')
