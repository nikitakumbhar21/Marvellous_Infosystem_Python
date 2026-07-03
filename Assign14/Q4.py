# Write lambda function to return minimum of number

MinNum = lambda a,b : a if a < b else b

def main():
    no1 = int(input("Enter first Numbers: "))
    no2 = int(input("Enter second Numbers: "))

    result = MinNum(no1,no2)

    print("Minimum of two number is: ", result)

if __name__ == "__main__":
    main()