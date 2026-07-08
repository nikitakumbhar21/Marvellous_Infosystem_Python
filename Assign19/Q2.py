# write a program which contains one lambda function which accepts two parameter and return its multiplication.

Mult = lambda No1, No2: No1 * No2

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    result = Mult(value1, value2)
    print(f"Multiplocation is: {result}")

if __name__ == "__main__":
    main()