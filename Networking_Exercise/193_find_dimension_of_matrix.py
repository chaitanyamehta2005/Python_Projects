"""
Question:
Original list:
[[1, 2], [2, 4]]
Dimension of the said matrix:
(2, 2)
Original list:
[[0, 1, 2], [2, 4, 5]]
Dimension of the said matrix:
(2, 3)
Original list:
[[0, 1, 2], [2, 4, 5], [2, 3, 4]]
Dimension of the said matrix:
(3, 3)
"""

def dimension(lst):
    row = len(lst)
    column = len(lst[0])
    return (row,column)

Original_list1 = [[1, 2], [2, 4]]
Original_list2 = [[0, 1, 2], [2, 4, 5]]
Original_list3 = [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
Original_list4 = [[0, 1, 2, 3], [2, 4, 5, 6], [2, 3, 4, 5],[8,8,8,8]]
Original_list5 = [[0, 1, 2, 3], [2, 4, 5, 6], [2, 3, 4, 5]]

print("Dimension of the  {0} matrix is : {1}".format(Original_list1,dimension(Original_list1)))
print("Dimension of the  {0} matrix is : {1}".format(Original_list2,dimension(Original_list2)))
print("Dimension of the  {0} matrix is : {1}".format(Original_list3,dimension(Original_list3)))
print("Dimension of the  {0} matrix is : {1}".format(Original_list4,dimension(Original_list4)))
print("Dimension of the  {0} matrix is : {1}".format(Original_list5,dimension(Original_list5)))




