# Write lambda function to return multiplication of two numbers

Mult = lambda a,b : a * b

def main():
    no1 = int(input("Enter number: "))
    no2 = int(input("Enter number: "))

    Ans = Mult(no1,no2)
    print("Multiplication of two number is: ",Ans)

if __name__ == "__main__":
    main()