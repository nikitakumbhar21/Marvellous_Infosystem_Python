# write a program which accept one number from user and displya below pattern
# Decreasing start pattern

def DecreaPattern(No):
    for i in range(No, 0, -1):
        for j in range(i):
            print("* ", end = " ")
        print()
    print()

def main():
    value = int(input("Enter number: "))

    DecreaPattern(value)

if __name__ == "__main__":
    main()
