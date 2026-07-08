# write a program which accept one number from user and check whether number is prime or not.

def PrimeNum(No):
    if No <= 1:   # 0 and 1 are not prime
        return False
    for i in range(2, int(No ** 0.5) + 1):  # check divisibility up to sqrt(No)
        if No % i == 0:
            return False
    return True

def main():
    value = int(input("Enter number: "))
    if PrimeNum(value):
        print(f"{value} is a Prime number")
    else:
        print(f"{value} is NOT a Prime number")

if __name__ == "__main__":
    main()
