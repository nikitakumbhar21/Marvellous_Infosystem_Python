# Write lambda function to return Cube of number

Cube = lambda No : No ** 3

def main():
    No = int(input("Enter A Number: "))

    print("Cube of",No,"is: ", Cube(No))

if __name__ == "__main__":
    main()
