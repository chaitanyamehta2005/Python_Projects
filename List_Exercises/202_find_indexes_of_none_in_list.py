"""
Original list:
[1, None, 5, 4, None, 0, None, None]
Indexes of all None items of the list:
[1, 4, 6, 7]
"""

def none_index_checker(lst):
    result = [i for i in range(len(lst)) if lst[i] is None]
    return result

lst1 = [1, None, 5, 4, None, 0, None, None]
print("Indexes of all None items of the list: {0}".format(none_index_checker(lst1)))

