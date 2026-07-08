# write a program which accept one number from user and return addition of digits in that number.

def SumDigits(No):
    Sum = 0 

    for i in str(abs(No)):
        Sum = Sum + int(i) 

    return Sum   

def main():
    number = int(input("Enter number: "))

    Ret = SumDigits(number)

    print(f"Addition of digits from {number} number is : {Ret}")

if __name__ == "__main__":
    main()
