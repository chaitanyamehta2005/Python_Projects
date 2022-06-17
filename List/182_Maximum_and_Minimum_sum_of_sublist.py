"""
Question:
Original list:
[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
Maximum sum of sub list of the said list of lists:
[2, 3, 5, 4]
Minimum sum of sub list of the said list of lists:
[1, 2, 1, 2]
"""
def max_sublist(lst):
    max = lst[0]
    sum_elem = sum(max)
    for i in range(len(lst)):
        if sum_elem< sum(lst[i]):
            sum_elem =sum(lst[i])
            max = lst[i]
    return max

def min_sublist(lst):
    min = lst[0]
    sum_elem = sum(min)
    for i in range(len(lst)):
        if sum_elem> sum(lst[i]):
            sum_elem =sum(lst[i])
            min = lst[i]
    return min


input_lst = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]

print("Maximum sum of sub list of the said list of lists: {0}".format(max_sublist(input_lst)))
print("Minimum sum of sub list of the said list of lists: {0}".format(min_sublist(input_lst)))
