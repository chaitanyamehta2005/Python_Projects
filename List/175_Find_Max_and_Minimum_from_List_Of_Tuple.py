"""
Question:
Original list:
[(2, 3), (2, 4), (0, 6), (7, 1)]
Maximum value for each tuple position in the said list of tuples:
[7, 6]
Minimum value for each tuple position in the said list of tuples:
[0, 1]
"""

def min_max(lst):
    """In this function, we use zip to iterate over all the elements of list and *lst to extract the list"""
    result_max = map(max, zip(*lst))
    result_min = map(min, zip(*lst))
    return list(result_max),list(result_min)


input_lst = [(2, 3), (2, 4), (0, 6), (7, 1)]
result = min_max(input_lst)

#Maximum values print
print("Maximum values of the list of tuple is {0}".format(result[0]))

#Minimum values print
print("Minimum values of the list of tuple is {0}".format(result[1]))

