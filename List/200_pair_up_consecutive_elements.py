"""
Original lists:
[1, 2, 3, 4, 5, 6]
Pair up the consecutive elements of the said list:
[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
Original lists:
[1, 2, 3, 4, 5]
Pair up the consecutive elements of the said list:
[[1, 2], [2, 3], [3, 4], [4, 5]]
"""


def pair_up_consecutive(lst):
    """In this method the result is achieved using simple for loop iteration"""
    result =[]
    for i in range (len(lst)-1):
        first_elem = lst[i]
        second_elem = lst[i+1]
        elem =[first_elem,second_elem]
        result.append(elem)
    return result

def pair_up_consecutive_v2(lst):
    """In this method the result is achieved using simple for loop iteration and list comprehension"""
    result = [[lst[i],lst[i+1]]for i in range(len(lst)-1)]
    return result

lst1 = [1, 2, 3, 4, 5, 6]
print("Pair up the consecutive elements of the said list(using simple for loop): {0}".format(pair_up_consecutive(lst1)))
print("Pair up the consecutive elements of the said list(using simple for loop and comprehension): {0}".format(pair_up_consecutive_v2(lst1)))
