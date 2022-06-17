"""
Original lists:
students = [u'S001', u'S002', u'S003', u'S004']
Convert the said unicode list to a list contains strings:
['S001', 'S002', 'S003', 'S004']
"""

def unicode_to_str(lst):
    result = [str(x) for x in lst]
    return result

students = [u'S001', u'S002', u'S003', u'S004']
print("Convert the said unicode list to a list contains strings: {0}".format(unicode_to_str(students)))