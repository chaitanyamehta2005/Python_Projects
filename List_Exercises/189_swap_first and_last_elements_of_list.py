"""
Question:
Original list:
[1, 2, 3, 4, 5, 6, 7]
Shift last element to first position and first element to last position of the said list:
[7, 2, 3, 4, 5, 6, 1]
Original list:
['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
Shift last element to first position and first element to last position of the said list:
['f', 'd', 'f', 'd', 's', 's', 'd', 's']
"""

def swap_element(lst):
    lst[0],lst[-1]=lst[-1],lst[0]
    return lst


orig_list = [1, 2, 3, 4, 5, 6, 7]
print("original list: {0}".format(orig_list))
print("Shift last element to first position and first element to last position of the said list: {0}".format(swap_element(orig_list)))

print("\n")
orig_list = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
print("original list: {0}".format(orig_list))
print("Shift last element to first position and first element to last position of the said list: {0}".format(swap_element(orig_list)))
