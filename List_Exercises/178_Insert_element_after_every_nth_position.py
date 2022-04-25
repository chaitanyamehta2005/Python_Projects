"""
Question:
Original list:
[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
Insert 20 in said list after every 4 th element:
[1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]
Original list:
['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
Insert Z in said list after every 3 th element:
['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']
"""

def elem_insert(lst,elem, pos):
    result = []
    for i in range(0,len(lst)):
        result.append(lst[i])
        if (i+1)%pos ==0:
            result.append(elem)
    return result

input_lst1 =[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
print(elem_insert(input_lst1,20,4))

input_lst2 =['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
print(elem_insert(input_lst2,'Z',3))