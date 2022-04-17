"""
Question:
Original list:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Insert a in the said list after 2 nd element:
[1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]
Insert b in the said list after 4 th element:
[1, 2, 3, 4, 'b', 5, 6, 7, 8, 'b', 9, 0]
"""
def insert_elem_pos(lst,elem,pos):
    output = []
    for i in range (0,len(lst),pos):
        output.extend(lst[i:i+pos])
        output.append(elem)
        output.pop()
    return output

# Take input list
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Insert a after every 2nd element
output_list_1= insert_elem_pos(input_list,'a',2)
print("new list after inserting a at after every 2nd element is : {0}".format(output_list_1))

# Insert b after every 3rd element
output_list_2= insert_elem_pos(input_list,'b',4)
print("new list after inserting b at after every 4th element is : {0}".format(output_list_2))