"""
Question:
Original list:
[1, 2, 3, 4, 5, 6, 7]
Sum the said list of numbers:
[1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
Original list:
[0, 1, -3, 3, 7, -5, 6, 7, 11]
Sum the said list of numbers:
[0.5, -1.0, 0.0, 5.0, 1.0, 0.5, 6.5, 9.0]
"""

def average_two_consecutive(lst):
   result = [(lst[i]+lst[i+1])/2 for i in range(len(lst)-1)]
   return result

orig_lst = [1, 2, 3, 4, 5, 6, 7]
print("Sum the said list of numbers: {0}".format(average_two_consecutive(orig_lst)))

orig_lst = [0, 1, -3, 3, 7, -5, 6, 7, 11]
print("Sum the said list of numbers: {0}".format(average_two_consecutive(orig_lst)))