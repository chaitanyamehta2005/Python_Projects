"""
Question:
Original list:
[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
Compute the sum of non-zero groups (separated by zeros) of the said list of numbers: [15, 38, 15, 27]
"""

def test(lst):
    sum_lst =[]
    previous =0

    for elem in lst:
        current = elem
        if previous !=0 and current !=0:
            sum = sum+current
        if previous ==0 and current !=0:
            sum = 0
            sum = sum+current
        if previous!=0 and current ==0:
            sum = sum + current
            sum_lst.append(sum)
        previous =current
    return sum_lst




orig_lst = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]

print(test(orig_lst))

