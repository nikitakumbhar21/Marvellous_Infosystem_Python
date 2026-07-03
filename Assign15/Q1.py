# Write a lambda function using map() which accepts list of numbers
# and returns list of squares of each numbers

Square = lambda No : No ** 2

def main():
    numbers = list(map(int, input("Enter list of numbers: ").split()))

    result = list(map(Square,numbers))

    print("List of square of each numbers:", result)
    


if __name__ == "__main__":
    main()