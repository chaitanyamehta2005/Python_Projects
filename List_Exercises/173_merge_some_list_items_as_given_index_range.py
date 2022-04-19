"""
Question:
Original lists:
['a', 'b', 'c', 'd', 'e', 'f', 'g']
Merge items from 2 to 4 in the said List:
['a', 'b', 'cd', 'e', 'f', 'g']
Merge items from 3 to 7 in the said List:
['a', 'b', 'c', 'defg']
"""

#The following function achieves using the concatanation of the given range
def merge_items(lst,index_start,index_end):
    output =lst
    output[index_start:index_end]= [''.join(output[index_start:index_end])]
    return output

original_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#Output
print(merge_items(original_lst,2,7))
