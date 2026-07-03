# Write a lambda function using filter() which accepts list of numbers
# and returns list of even numbers

EvenNum = lambda No : No % 2 == 0

def main():
    numbers = list(map(int, input("Enter list of numbers: ").split()))

    result = list(filter(EvenNum,numbers))

    print("List of even numbers:", result)

if __name__ == "__main__":
    main()