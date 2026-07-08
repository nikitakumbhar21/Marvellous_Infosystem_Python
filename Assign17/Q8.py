# write a program which accept one number from user and displya below pattern
# Decreasing start pattern

def DecreaPattern(No):
    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j, end = " ")
        print()
    print()

def main():
    value = int(input("Enter number: "))

    DecreaPattern(value)

if __name__ == "__main__":
    main()
