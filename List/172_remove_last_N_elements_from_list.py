"""
Question:
Original lists:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
Remove the last 3 elements from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
Remove the last 5 elements from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
Remove the last 1 element from the said list:
[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]
"""
#Following function removes last N elements from list
def remove_N_elem(lst,N):
    for i in range (0,N):
        if lst ==[]:
            print("Sorry, the list is empty. Nothing to remove")
            return
        lst.pop()
    return lst

orig_list= [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]

output_1 = remove_N_elem(orig_list,10)
print(output_1)