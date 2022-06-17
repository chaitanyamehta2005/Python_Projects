import csv

def read_column(csv_filename, column_name):
    with open(csv_filename) as file:
        csv_data = csv.DictReader(file)
        colum_list = []
        for row in csv_data:
            var_name = row[column_name]
            colum_list.append(var_name)
        return colum_list


def read_row(csv_filename, row_number):
    row_lst = []
    with open(csv_filename) as file:
        csv.data = csv.reader(file, delimiter=',')
        for row in csv.data:
            row_lst.append(row)
        return (row_lst[row_number])


print(read_column('data.csv', 'age'))
print(read_row('data.csv', 3))
