"""
Question:
Original lists:
[2, 3, 5, 8, 7, 2, 3]
[4, 3, 9, 0, 4, 3, 9]
[2, 1, 5, 6, 5, 5, 4]
Maximum value of the said three lists:
9
Minimum value of the said three lists:
0
"""

lst1 = [2, 3, 5, 8, 7, 2, 3]
lst2 = [4, 3, 9, 0, 4, 3, 9]
lst3 = [2, 1, 5, 6, 5, 5, 4]

max_of_lists = max(lst1 +lst2 +lst3)
min_of_lists = min(lst1 +lst2 +lst3)
print("Maximum value of the said three lists: {0}".format(max_of_lists))
print("Minimum value of the said three lists: {0}".format(min_of_lists))
