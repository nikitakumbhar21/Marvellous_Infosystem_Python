# Check prime number
def isPrime(number):
    if number <= 1:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
             return False
        return True

def main():
    No = int(input("Enter the number: "))

    if isPrime(No):
        print(No,"is Prime Number")
    else: 
        print(No,"is not Prime Number")

if __name__ == "__main__":
    main()