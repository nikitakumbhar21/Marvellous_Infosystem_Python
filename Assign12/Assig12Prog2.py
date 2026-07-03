#   Print Factors of a Number
def main():
    Number = int(input("Enter a number: "))

    print("Factors of",Number,"are:",end =" ")
    for i in range(1, Number + 1):
        if Number % i == 0:
            print(i, end =" ")
    print()

if __name__ == "__main__":
    main()