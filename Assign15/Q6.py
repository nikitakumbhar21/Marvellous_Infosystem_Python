# Write a lambda function using reduce() which accepts list of numbers
# and returns minimum elements

from functools import reduce
Min = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    numbers = list(input("Enter list of numbers: ").split())

    result = reduce(Min,numbers)

    print("Minimum of two numbers:", result)

if __name__ == "__main__":
    main()