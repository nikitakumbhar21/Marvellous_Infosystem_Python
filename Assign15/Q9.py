# Write a lambda function using reduce() which accepts list of numbers
# and returns product of all elements

from functools import reduce
ProdNum = lambda no1, no2 : no1 * no2

def main():
    numbers = list(map(int,input("Enter list of numbers: ").split()))

    result = reduce(ProdNum,numbers)

    print("Product of all elements from list: ", result)

if __name__ == "__main__":
    main()