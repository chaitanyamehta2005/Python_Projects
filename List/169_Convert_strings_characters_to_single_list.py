"""
Question:
Original list:
['red', 'white', 'a', 'b', 'black', 'f']
Convert the said list of strings and characters to a single list of characters:
['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']
"""

input_lst=['red', 'white', 'a', 'b', 'black', 'f']

# Double for loop in list comprehension
output_lst = [ i for element in input_lst for i in element]
print(output_lst)