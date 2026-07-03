# Write a lambda function using filter() which accepts list of numbers
# and returns list of odd numbers

OddNum = lambda No : No % 2 != 0

def main():
    numbers = list(map(int, input("Enter list of numbers: ").split()))

    result = list(filter(OddNum,numbers))

    print("List of odd numbers:", result)

if __name__ == "__main__":
    main()