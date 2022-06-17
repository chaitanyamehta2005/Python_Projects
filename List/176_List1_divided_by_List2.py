"""
Original list:
[7, 2, 3, 4, 9, 2, 3]
[9, 8, 2, 3, 3, 1, 2]
[0.7777777777777778, 0.25, 1.5, 1.3333333333333333, 3.0, 2.0, 1.5]
"""

input_lst1 = [7, 2, 3, 4, 9, 2, 3]
input_lst2 = [9, 8, 2, 3, 3, 1, 2]

# List comprehension using the zip function for two lists.
output_lst = [a/b for a,b in zip(input_lst1,input_lst2)]

print(output_lst)