# Write lambda function to return True if number is Odd otherwise False

CheckOdd = lambda No : True if No % 2 != 0 else False

def main():
    x = int(input("Enter number: "))

    result = CheckOdd(x)

    print(result)

if __name__ == "__main__":
    main()