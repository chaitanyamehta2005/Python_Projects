"""
Question:
Original list:
[3, 40, 41, 43, 74, 9]
Largest possible number using the elements of the said list of positive integers:
9744341403
Original list:
[10, 40, 20, 30, 50, 60]
Largest possible number using the elements of the said list of positive integers:
605040302010
Original list:
[8, 4, 2, 9, 5, 6, 1, 0]
Largest possible number using the elements of the said list of positive integers:
98654210
"""


def create_num_v1(lst):
    result = ''.join(sorted((str(val) for val in lst), reverse=True, key=lambda i: i * (len(str(max(lst))) * 2 // len(i))))
    return result

input_lst1 = [8, 4, 2, 9, 5, 6, 1, 0]
reversed = sorted(input_lst1, reverse=True)

result = create_num_v1(reversed)

print(" Largest possible number using the elements of the said list of positive integers: {0}".format(result))
