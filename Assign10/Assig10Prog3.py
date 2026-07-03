def main():
    No = int(input("Enter Number: "))

    Fact = 1

    if No < 0:
        print("Factorial does not exit for negative numbers")
    else:
        for i in range(1, No + 1):
            Fact = Fact * i
        print("Facrorial of",No,"is : ", Fact)

if __name__ == "__main__":
    main()