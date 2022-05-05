"""
Question:
Original list:
[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
Average of n-th elements in the said list of lists with different lengths:
[4.8, 5.8, 6.8, 8.0, 11.0]
"""
import itertools

def get_avg(x):
    x = [ i for i in x if i is not None]
    return sum(x)/len(x)

origninal_lst = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
result = map(get_avg,itertools.zip_longest(*origninal_lst))
print(list(result))

