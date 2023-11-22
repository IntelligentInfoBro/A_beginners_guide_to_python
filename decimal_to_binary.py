# decimal_to_binary.py
#
# Description: 
# This code takes a string of space-separated decimal numbers as input,
# converts each decimal number into its binary representation, and prints
# the binary representations as space-separated output. The `encode_byte`
# function is used to perform the conversion from decimal to binary.
#
# Author: Chaitanya Mittal
# Date: 2023-11-22 10:09:00.941632

# ASSUMPTION: Well behaved user that enters input as 1-space separated string
#             of decimals.

"""IDEA:
- define a function to encode byte:
    get the decimal
    encode the decimal into byte
    return the byte
- get input of the decimal
- traverse using for loop for each decimal (after removing space)
- convert to byte
- add this to answer list
- print space separated answer"""

def encode_byte(decimal):
    """
    Function to encode a decimal number into binary.

    Parameters:
    decimal (int): The decimal number to be converted.

    Returns:
    str: The binary representation of the decimal number.
    """
    answer = ""
    # loop from 7 to 0 (reverse order) with step -1
    for i in range(7, -1, -1):
        # calculate binary representation at each step
        binary = (decimal // 2**i)
        # update decimal value by taking modulo at each step
        decimal = decimal % 2**i
        # append binary value to answer string
        answer += str(binary)
    return(answer)

#get the input as string
string = input("Enter string of space-separated decimals: ")
# remove the leading and trailing spaces
#
decimal_lst = string.split()
binary_lst = []
for decimal in decimal_lst:
    binary = encode_byte(int(decimal))
    binary_lst.append(binary)

# print space separated binary values
print(' '.join(binary_lst))

