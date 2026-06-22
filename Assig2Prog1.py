# Write a program to display :
# Data type
# Memory address
# Size in bytes of a variable entered by the user
# -------------------------------------------------------------------------

import sys

print("Enter any data: ")
x = int(input())

print("Data type of variable is: ", type(x))
print("Memory address of variable is: ",id(x))
print("Size of bytes for variable : ", sys.getsizeof(x))