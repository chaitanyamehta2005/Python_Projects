"""
Question:
Sample Output:
After merging lists into a list of lists:
[['a', 1, True], ['b', 2, False]]
[['a', 1, True], [None, 2, False]]
[['a', 1, True], ['_', 2, False]]
"""

def merge_lists(lst1,lst2):
    return [lst1,lst2]

lst1 = ['a', 1, True]
lst2 = ['b', 2, False]
print(merge_lists(lst1,lst2))
