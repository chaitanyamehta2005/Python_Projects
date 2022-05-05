"""
Question:
Original list:
['red', 'green', 'white', 'black']
Traverse the said list in reverse order:
black
white
green
red
Traverse the said list in reverse order with original index:
3 black
2 white
1 green
0 red
"""

Original_list=['red', 'green', 'white', 'black']

# First section of desired output:
print("Traverse the said list in reverse order:")
for i in range(len(Original_list)-1, -1,-1):
    print(Original_list[i])


# Second section of desired output:
print("Traverse the said list in reverse order with original index:")
for i in range(len(Original_list)-1, -1,-1):
    print("{0} {1}".format(i,Original_list[i]))

