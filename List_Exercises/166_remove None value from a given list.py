"""
Question:
Original list:
[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
Remove None value from the said list:
[12, 0, 23, -55, 234, 89, 0, 6, -12]
"""
# First take a list with some elements as None.
input_lst1= [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

#Now create a list comprehension after removing the None values
output_lst = [input_lst1[i] for i in range (len(input_lst1)) if input_lst1[i] is not None]
print("output after removal of None is {0}".format(output_lst))