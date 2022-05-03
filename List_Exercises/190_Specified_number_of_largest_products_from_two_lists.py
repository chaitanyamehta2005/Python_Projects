"""
Question:
Original lists:
[1, 2, 3, 4, 5, 6]
[3, 6, 8, 9, 10, 6]
3 Number of largest products from the said two lists:
[60, 54, 50]
4 Number of largest products from the said two lists:
[60, 54, 50, 48]
"""

def largest_product(lst1,lst2,n):
    result = sorted([x*y for x in lst1 for y in lst2], reverse=True)[:n]

    return result[:n]


lst1 = [1, 2, 3, 4, 5, 6]
lst2 =[3, 6, 8, 9, 10, 6]
n = int(input(" How many products do you require ?: "))
print("{0} Number of largest products from the said two lists: {1}".format(n,largest_product(lst1,lst2,n)))

