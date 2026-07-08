# write a program which accept one number from user and return its factorial.

def Factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i 
    return Fact
    print()

def main():
    value = int(input("Enter number: "))

    result = Factorial(value)

    print(f"Factorial of number is: {result}")

if __name__ == "__main__":
    main()