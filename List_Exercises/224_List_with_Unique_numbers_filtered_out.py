"""
Question:
Original List: [1, 2, 2, 3, 4, 4, 5]
Sample Output: [2,4]
"""

def unique_filter(lst):
    result = [x for x in lst if ((lst.count(x)!=1))]
    result = list(set(result)) # For removing the multiple entries from the output
    return result

Orig_List =  [1, 2, 2, 3, 4, 4, 5]
print("Filtered out the non unique values from list and final output is  {0}".format(unique_filter(Orig_List)))