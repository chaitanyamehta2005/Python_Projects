"""
Question:
Original Number: 8
Decimal number ( 8 ) to binary list:
[1, 0, 0, 0]
Original Number: 45
Decimal number ( 45 ) to binary list:
[1, 0, 1, 1, 0, 1]
Original Number: 100
Decimal number ( 100 ) to binary list:
[1, 1, 0, 0, 1, 0, 0]
"""

def decimal_to_binary(num):
    """Mathematical formula for decimal to binary = keep divide by 0 and append remainder to the output list"""
    result=[]
    while (num>0):
        rem = (num%2)
        result.append((rem))
        num = num//2
    result.reverse()
    return result

decimal_number = int(input("Enter any whole decimal number: "))
print("Decimal number {0} to binary list: {1}".format(decimal_number,decimal_to_binary(decimal_number)))