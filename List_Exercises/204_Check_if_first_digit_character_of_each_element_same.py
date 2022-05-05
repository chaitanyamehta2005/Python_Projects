"""
Question:
Original list:
[1234, 122, 1984, 19372, 100]
Check if first digit in each element of the said given list is same or not!
True
Original list:
[1234, 922, 1984, 19372, 100]
Check if first digit in each element of the said given list is same or not!
False
Original list:
['aabc', 'abc', 'ab', 'a']
Check if first character in each element of the said given list is same or not!
True
Original list:
['aabc', 'abc', 'ab', 'ha']
Check if first character in each element of the said given list is same or not!
False
"""

def first_digit_char_checker(lst):
    """This method check the first character(digit) of first element and compares all the other element's first character(digit)"""
    element1 =str(lst[0])
    for i in lst:
        if str(i).startswith(element1[0]):
            continue
        else:
            return False
    return True

lst = [1234, 122, 1984, 19372, 100]
print(first_digit_char_checker(lst))

lst = [1234, 922, 1984, 19372, 100]
print(first_digit_char_checker(lst))

lst = ['aabc', 'abc', 'ab', 'a']
print(first_digit_char_checker(lst))

lst = ['aabc', 'abc', 'ab', 'ha']
print(first_digit_char_checker(lst))

