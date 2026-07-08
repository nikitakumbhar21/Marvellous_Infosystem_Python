# write a program which contains one lambda function which accepts one parameter and return power of two

PowerOf = lambda No: No ** 2

def main():
    value = int(input("Enter number: "))

    result = PowerOf(value)
    print(f"Power of {value} is: {result}")

if __name__ == "__main__":
    main()