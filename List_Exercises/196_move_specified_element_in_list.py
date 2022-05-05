"""
Original list:
['red', 'green', 'white', 'black', 'orange']
Move white at the end of the said list:
['red', 'green', 'black', 'orange', 'white']
Original list:
['red', 'green', 'white', 'black', 'orange']
Move red at the end of the said list:
['green', 'white', 'black', 'orange', 'red']
Original list:
['red', 'green', 'white', 'black', 'orange']
Move black at the end of the said list:
['red', 'green', 'white', 'orange', 'black']
"""


def move_to_end(lst,elem):
    lst.remove(elem)
    lst.append(elem)
    return lst

orig_lst = ['red', 'green', 'white', 'black', 'orange']
specified_element = 'white'
print("Move {0} at the end of the said list: {1}".format(specified_element,move_to_end(orig_lst,specified_element)))

orig_lst = ['red', 'green', 'white', 'black', 'orange']
specified_element = 'red'
print("Move {0} at the end of the said list: {1}".format(specified_element,move_to_end(orig_lst,specified_element)))

orig_lst = ['red', 'green', 'white', 'black', 'orange']
specified_element = 'black'
print("Move {0} at the end of the said list: {1}".format(specified_element,move_to_end(orig_lst,specified_element)))
