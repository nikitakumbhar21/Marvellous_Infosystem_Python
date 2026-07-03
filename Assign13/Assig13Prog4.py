#   Print Binary equivalent
def main():
    number = int(input("Enter number:"))

    binary_equivalent = bin(number)[2:]

    print("Binary equivalent: ", binary_equivalent)

if __name__ == "__main__":
    main()