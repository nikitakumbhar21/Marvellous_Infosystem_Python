# Write program which contains one function name as Add() which accepts two numbers from uset and
# return addition of that two numbers.
def Add(no1,no2):
    ans = no1 + no2
    return ans


def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    result = Add(value1, value2)

    print(f"Addition of two number is: {result}")

if __name__ == "__main__":
    main()