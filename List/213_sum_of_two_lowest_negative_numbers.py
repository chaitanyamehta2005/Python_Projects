"""
Question:
An integer (from the Latin integer meaning "whole") is colloquially defined as a number that can be written without a fractional component. For example, 21, 4, 0, and -2048 are integers.
Original list elements: [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
Sum of two lowest negative numbers of the said array of integers: -27
Original list elements: [-4, 5, -2, 0, 3, -1, 4, 9]
Sum of two lowest negative numbers of the said array of integers: -6
"""


def sum_two_lowest_negative_int(lst):
    result = sorted([x for x in lst if x<0])
    sum = result[0]+result[1]
    return sum

orig_list = [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
print("Sum of two lowest negative numbers of the said array of integers: {0}".format(sum_two_lowest_negative_int(orig_list)))

orig_list = [-4, 5, -2, 0, 3, -1, 4, 9]
print("Sum of two lowest negative numbers of the said array of integers: {0}".format(sum_two_lowest_negative_int(orig_list)))