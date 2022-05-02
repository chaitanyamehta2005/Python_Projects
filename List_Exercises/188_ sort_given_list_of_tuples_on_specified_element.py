"""
Question:
Original list of tuples:
[('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
Sort on 1st element of the tuple of the said list:
[('item1', 11, 24.5), ('item2', 10, 10.12), ('item3', 15, 25.1), ('item4', 12, 22.5)]
Sort on 2nd element of the tuple of the said list:
[('item2', 10, 10.12), ('item1', 11, 24.5), ('item4', 12, 22.5), ('item3', 15, 25.1)]
Sort on 3rd element of the tuple of the said list:
[('item2', 10, 10.12), ('item4', 12, 22.5), ('item1', 11, 24.5), ('item3', 15, 25.1)]
"""
def sort_elem(lst,n):
    result =sorted((lst), key =lambda x: x[n-1])
    return result

orig_list =[('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
n = int(input("On which element you want to sort out the list of tuples {0} ? :".format(orig_list)))

print("Sort on {0}th element of the tuple of the said list: {1}".format(n, sort_elem(orig_list,n)))
