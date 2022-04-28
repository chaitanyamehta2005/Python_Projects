"""
Question:
Original list:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
Iterate the said list cyclically on specific index position 3 :
['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
Iterate the said list cyclically on specific index position 5 :
['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']
"""

def cyclic(lst,pos):
    """ Use the slicing operation of List and concatanation"""
    output =lst[pos:]+lst[:pos]
    return output

input_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("Original list is: {0}".format(input_lst))
print("Iterate the said list cyclically on specific index position 3 : {}".format(cyclic(input_lst,3)))