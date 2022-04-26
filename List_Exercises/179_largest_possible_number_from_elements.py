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
    result = int("".join(map(str, lst)))
    return result

def create_num_v2(lst):
    result=''
    for i in lst:
        result=result+str(i)
    return result

input_lst1 = [10, 40, 20, 30, 50, 60]
reversed = sorted(input_lst1, reverse=1)

#This is the fist method of creating number out of the list.
result = create_num_v1(reversed)

#This is the second method of creating number out of the list.
result2 = create_num_v2(reversed)

print(" Largest possible number using the elements of the said list of positive integers: {0}".format(result))

print(" Largest possible number using the elements of the said list of positive integers: {0}".format(result2))
