"""
Question:
Original list:
['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
Remove additional spaces from the said list:
['abc', '', '', 'sdfds', '', '', 'sdfds', 'huy']
"""

def remove_spaces(lst):
    result = []
    for i in lst:
        if ' ' in i:
            result.append(i.strip(' '))
        else:
            result.append(i)

    return result

orig_list = ['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
print("Remove additional spaces from the said list: {0}".format(remove_spaces(orig_list)))
