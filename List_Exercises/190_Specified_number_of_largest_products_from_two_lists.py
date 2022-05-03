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
import itertools

def largest_product(lst1,lst2,n):
    result = sorted([x*y for x in lst1 for y in lst2], reverse=True)[:n]

    return result[:n]

def largest_product_v2(lst1,lst2,n):
    """This is another method using the intertool to achieve the same output"""
    result = []
    result = sorted([v1*v2 for v1, v2 in itertools.product(lst1, lst2)],reverse=True)
    return(result[:n])


lst1 = [1, 2, 3, 4, 5, 6]
lst2 =[3, 6, 8, 9, 10, 6]
n = int(input(" How many products do you require ?: "))
print("{0} Number of largest products from the said two lists using method1: {1}".format(n,largest_product(lst1,lst2,n)))
print("{0} Number of largest products from the said two lists using method2: {1}".format(n,largest_product_v2(lst1,lst2,n)))
