"""
Question:
Original list of strings:
['Red', 'Maroon', 'Yellow', 'Olive']
Convert the said list of strings into list of lists:
[['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]
"""
# Take an input with multple string elements
input_lst= ['Red', 'Maroon', 'Yellow', 'Olive']

# List comprehension for conversion from string to list
output_lst = [list(input_lst[i]) for i in range (len(input_lst)) ]
print("output list after conversion from string to list is:  {0}".format(output_lst))


