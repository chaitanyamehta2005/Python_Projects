"""
Question:
Original list:
['Ricky Rivera', 98, 'Math', 90, 'Science']
After deleting an element 'Ricky Rivera':, using index of the element: [98, 'Math', 90, 'Science']
"""

def remove_elem(lst,elem):
    lst.remove(elem)
    return lst

orig_lst = ['Ricky Rivera', 98, 'Math',90, 'Science']
print("After deleting an element {0}:, using index of element: {1}".format('Ricky Rivera',remove_elem(orig_lst,'Ricky Rivera')))
