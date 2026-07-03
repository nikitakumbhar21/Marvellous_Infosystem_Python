# Write lambda function to return square of number

Sqaure = lambda No : No ** 2

def main():
    No = int(input("Enter A Number: "))

    print("Sqaure of",No,"is: ", Sqaure(No))

if __name__ == "__main__":
    main()
