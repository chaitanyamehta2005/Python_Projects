"""
Question:
Original lists:
['0', '1', '2', '3', '4']
['red', 'green', 'black', 'blue', 'white']
['100', '200', '300', '400', '500']
Concatenate element-wise three said lists:
['0red100', '1green200', '2black300', '3blue400', '4white500']
"""

lst1=['0', '1', '2', '3', '4']
lst2=['red', 'green', 'black', 'blue', 'white']
lst3=['100', '200', '300', '400', '500']

#Take an empty list for output
output_list=[]

#Use the zip function and then concatenate  & append the output list.
for a,b,c in zip(lst1,lst2,lst3):
    output_list.append(a+b+c)

print(output_list)