"""
Question:
Original list:
[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
Unique values of the said list of lists:
[0, 1, 2, 3, 4, 5, 7]
Original list:
[['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
Unique values of the said list of lists:
['e', 'd', 'c', 'b', 'x', 'k', 'n', 'h', 'g', 'j', 'i', 'a', 'l', 'y', 'v', 'z']
"""


input_list= [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]

# Here we have used Set and its union method for finding the unique values from the list of lists and also we are using list unpacking.
output_lst = list(set(input_list[0]).union(*input_list))
print("Unique values of the said list of lists: {0}".format(output_lst))

input_list= [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
output_lst = list(set(input_list[0]).union(*input_list))
print("Unique values of the said list of lists: {0}".format(output_lst))