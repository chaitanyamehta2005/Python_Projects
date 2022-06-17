"""
Question:
Original list:
[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
Compute the sum of non-zero groups (separated by zeros) of the said list of numbers: [15, 38, 15, 27]
"""

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def test(lst):
    sum_list = []
    sum = 0

    for elem in lst:
        if int(elem) != 0:
            sum = sum + int(elem)
        else:
            if sum != 0:
                sum_list.append(sum)
            sum = 0
    sum_list.append(sum)
    return sum_list

orig_lst = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]

print(test(orig_lst))

