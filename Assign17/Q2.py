# write a program which accept one number and display below pattern.
# Square matrix patterm

def DisplayPattern(No):
    print("Output is: ")
    print()

    for i in range(No):
        for j in range(No):
            print("* ", end = " ")
        print()
    print()

def main():
    value = int(input("Enter number: "))

    DisplayPattern(value)

if __name__ == "__main__":
    main()