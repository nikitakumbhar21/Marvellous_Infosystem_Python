# write a program which accept one number from user and return number of digits in that number.

def NumDigits(No):
    return len(No)

def main():
    value = input("Enter number: ")

    Ret = NumDigits(value)

    print(f"Number of digits from {value} number is : {Ret}")

if __name__ == "__main__":
    main()
