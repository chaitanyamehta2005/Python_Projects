"""
Question:
Original list:
[1234, 1522, 1984, 19372, 1000, 2342, 7626]
Indices of elements of the said list, greater than 3000
[3, 6]
Original list:
[1234, 1522, 1984, 19372, 1000, 2342, 7626]
Indices of elements of the said list, greater than 20000
[]
"""

def comparator(lst,value):
    return [i for i in range(len(lst)) if lst[i]>value ]

lst = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
compare_value = int(input("For the list {0} give the value you want to compare: ".format(lst)))
print("Indices of elements of the said list, greater than {0} is {1}".format(compare_value,comparator(lst,compare_value)))
