"""
Original list:
[[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
Common elements of the said list of lists:
[2, 3]
Original list:
[['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
Common elements of the said list of lists:
['c']
"""
def common_elem(lst):
    """This method is using the set intersection to derive the common elements"""
    result = set(lst[0]).intersection(*lst)
    return list(result)


input_lst1 = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
print("Original list is {0}".format(input_lst1))
print("Common elements of the said list of lists: {0}".format(common_elem(input_lst1)))

print("\n")

input_lst2 = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
print("Original list is {0}".format(input_lst2))
print("Common elements of the said list of lists: {0}".format(common_elem(input_lst2)))