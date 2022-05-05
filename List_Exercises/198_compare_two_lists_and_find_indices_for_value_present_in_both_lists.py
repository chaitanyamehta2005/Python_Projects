"""
Question:
Original lists:
[1, 2, 3, 4, 5, 6]
[7, 8, 5, 2, 10, 12]
Compare said two lists and get the indices of the values present in both lists:
[1, 4]
Original lists:
[1, 2, 3, 4, 5, 6]
[7, 8, 5, 7, 10, 12]
Compare said two lists and get the indices of the values present in both lists:
[4]
Original lists:
[1, 2, 3, 4, 15, 6]
[7, 8, 5, 7, 10, 12]
Compare said two lists and get the indices of the values present in both lists:
[]
"""

def find_indices_common_elem(lst1,lst2):
    common_elem = list(set(lst1).intersection(set(lst2)))
    result = [lst1.index(elem)for elem in common_elem]
    return result


lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [7, 8, 5, 2, 10, 12]

print("Compare said two lists and get the indices of the values present in both lists: {0}" .format(find_indices_common_elem(lst1,lst2)))