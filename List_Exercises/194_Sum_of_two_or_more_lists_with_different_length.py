"""
Question:
Original list:
[[1, 2, 4], [2, 4, 4], [1, 2]]
Sum said lists with different lengths:
[4, 8, 8]
Original list:
[[1], [2, 4, 4], [1, 2], [4]]
Sum said lists with different lengths:
[8, 6, 4]
"""
import itertools

orig_lst = [[1], [2, 4, 4], [1, 2], [4]]

#zip function by default iterates over shortest length so that used itertools zip longest alongwith fillvalue =0
# Reference: https://www.youtube.com/watch?v=3n7Z99_cV2Y
result = [sum(x) for x in itertools.zip_longest(*orig_lst, fillvalue=0)]

print("Sum said lists with different lengths: {0}".format(result))