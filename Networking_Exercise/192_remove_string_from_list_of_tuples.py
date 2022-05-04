"""
Question:
Original list:
[(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
Remove all strings from the said list of tuples:
[(100,), (80,), (90,), (88, 89), (90, 92)]
"""


def remove_string(lst):
    """ List comprehension cascaded and find the data type = string and ignored in the output"""
    output = [tuple (v for v in i if not isinstance(v, str)) for i in lst]
    return output

orig_list = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
print(remove_string(orig_list))


