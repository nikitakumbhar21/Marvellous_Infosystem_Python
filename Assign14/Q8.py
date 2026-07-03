# Write lambda function to return addition of two numbers

Addition = lambda a,b : a + b

def main():
    no1 = int(input("Enter number: "))
    no2 = int(input("Enter number: "))

    Ans = Addition(no1,no2)
    print("Addition of two number is: ",Ans)

if __name__ == "__main__":
    main()