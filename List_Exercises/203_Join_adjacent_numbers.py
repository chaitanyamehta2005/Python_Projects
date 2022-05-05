"""
Question:
Original list:
['1', '2', '3', '4', '5', '6', '7', '8']
Join adjacent members of a given list:
['12', '34', '56', '78']
Original list:
['1', '2', '3']
Join adjacent members of a given list:
['12']
"""

def join_adj_nums(lst):
    """ returns the list of list comprehension with pairing of two elements"""
    return [str(lst[i])+str(lst[i+1])for i in range(0,len(lst)-1,2)]


orig_list = ['1', '2', '3', '4', '5', '6', '7', '8']
print("Join adjacent members of a given list: {0}".format(join_adj_nums(orig_list)))

orig_list = ['1', '2', '3']
print("Join adjacent members of a given list: {0}".format(join_adj_nums(orig_list)))