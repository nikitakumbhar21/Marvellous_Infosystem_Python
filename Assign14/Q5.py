# Write a program to return True if number is even otherwise False

CheckEven = lambda No : True if No % 2 == 0 else False

def main():
    x = int(input("Enter number: "))

    result = CheckEven(x)

    print(result)

if __name__ == "__main__":
    main()