"""
Question:
Original lists:
[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
[('red', 'green'), ('orange', 'pink')]
Common tuples between two said lists
[('orange', 'pink'), ('red', 'green')]
Original lists:
[('red', 'green'), ('orange', 'pink')]
[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
Common tuples between two said lists
[('orange', 'pink'), ('red', 'green')]
"""

def common_tuples(lst1,lst2):
    return(list(set(lst1).intersection(set(lst2))))

lst1 =[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
lst2 = [('red', 'green'), ('orange', 'pink')]

print("Common tuples between two said lists {0}".format((common_tuples(lst1,lst2))))

lst1 =[('red', 'green'), ('orange', 'pink')]
lst2 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]

print("Common tuples between two said lists {0}".format((common_tuples(lst1,lst2))))