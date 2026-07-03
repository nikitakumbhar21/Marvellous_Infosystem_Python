def main():
    No = int(input("Enter Number: "))

    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + i
    print("Sum of first", No,"natural numbers: ", Sum)

if __name__ == "__main__":
    main()