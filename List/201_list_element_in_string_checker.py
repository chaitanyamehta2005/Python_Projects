"""
Question:
The original string and list:
https://www.w3resource.com/python-exercises/list/
['.com', '.edu', '.tv']
Check if https://www.w3resource.com/python-exercises/list/ contains an element, which is present in the list ['.com', '.edu', '.tv']
True
The original string and list: https://www.w3resource.net
https://www.w3resource.net
['.com', '.edu', '.tv']
Check if https://www.w3resource.net contains an element, which is present in the list ['.com', '.edu', '.tv']
False
"""


def elem_checker(lst,str):
    for i in lst:
        if i in str:
            return True
    return False


string = 'https://www.w3resource.com/python-exercises/list/'
lst1 = ['.com', '.edu', '.tv']
print(elem_checker(lst1,string))

string = 'https://www.w3resource.net'
lst1 = ['.com', '.edu', '.tv']
print(elem_checker(lst1,string))