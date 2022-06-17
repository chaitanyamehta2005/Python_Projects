"""
Descending -> Highest to lowest.
Ascending -> Lowest to highest
Original Number: 134543
Descending order of the said number: 544331
Ascending order of the said number: 133445
Original Number: 43750973
Descending order of the said number: 97754330
Ascending order of the said number: 3345779
"""

def descending(num):
    desc_str = reversed((sorted(list(str(num)))))
    desc = int(str.join('',desc_str))
    return desc

def ascending(num):
    asc_str = (sorted(list(str(num))))
    asc = int(str.join('',asc_str))
    return asc

orig_num = int(input("Enter any positive integer number: "))
if (orig_num >=0):
    print("Descending order of the said number: {0}".format(descending(orig_num)))
    print("Ascending order of the said number: {0}".format(ascending(orig_num)))
else:
    print("Not a positive integer; Please check the input")

