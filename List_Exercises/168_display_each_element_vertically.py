"""
Question:
Original list:
['a', 'b', 'c', 'd', 'e', 'f']
Display each element vertically of the said list:
a
b
c
d
e
f
Original list:
[[1, 2, 5], [4, 5, 8], [7, 3, 6]]
Display each element vertically of the said list of lists:
1 4 7
2 5 3
5 8 6
"""
# Note: Though the expected outcome is similar for both the of above sub questions but the solutions will be different.

# Solution for first sub question
input_lst =['a', 'b', 'c', 'd', 'e', 'f']
for i in input_lst:
    print(i)

# Solution for second sub question
# We will use the zip function as each element has three sub elements.

input_lst =[[1, 2, 5], [4, 5, 8], [7, 3, 6]]
for a,b,c in zip(*input_lst):
    print("{0} {1} {2}".format(a,b,c))
