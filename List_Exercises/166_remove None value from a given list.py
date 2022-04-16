"""
Original list:
[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
Remove None value from the said list:
[12, 0, 23, -55, 234, 89, 0, 6, -12]
"""

lst1= [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
output = [lst1[i] for i in range (len(lst1)) if lst1[i] is not None]
print(output)