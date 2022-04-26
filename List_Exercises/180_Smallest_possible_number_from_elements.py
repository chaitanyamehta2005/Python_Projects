"""
Question:
Original list:
[3, 40, 41, 43, 74, 9]
Smallest possible number using the elements of the said list of positive integers:
3404143749
Original list:
[10, 40, 20, 30, 50, 60]
Smallest possible number using the elements of the said list of positive integers:
102030405060
Original list:
[8, 4, 2, 9, 5, 6, 1, 0]
Smallest possible number using the elements of the said list of positive integers:
01245689
"""


def create_num_v1(lst):
    result = ''.join(sorted((str(val) for val in lst), key=lambda i: i * (len(str(max(lst))) * 2 // len(i))))
    return result

input_lst1 = [8, 4, 2, 9, 5, 6, 1, 0]
reversed = sorted(input_lst1)

result = create_num_v1(input_lst1)

print(" Smallest possible number using the elements of the said list of positive integers: {0}".format(result))
