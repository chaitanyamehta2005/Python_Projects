"""
Question:
Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']
After removing all the values except integer values from the said array of mixed values: [12, 0]
"""

def remove_except_int(lst):
    return [result for result in lst if type(result)==int]

lst = [34.67, 12, -94.89, 'Python', 0, 'C#']
print("After removing all the values except integer values from the said array of mixed values: {0}".format(remove_except_int(lst)))