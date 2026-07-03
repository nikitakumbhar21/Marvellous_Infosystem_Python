# Write a lambda function using reduce() which accepts list of numbers
# and returns addition of all elements

from functools import reduce

Addition = lambda No1, No2 : No1 + No2

def main():
    numbers = list(map(int, input("Enter list of numbers: ").split()))

    result = reduce(Addition,numbers)

    print("Addition of all elements:", result)

if __name__ == "__main__":
    main()