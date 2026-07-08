# write a program which accept one number and display below pattern
# Repeated Number Grid

def DecreaPattern(No):
    for i in range(No):
        for j in range(1,No+1):
            print(j , end = " ")
        print()
    print()

def main():
    value = int(input("Enter number: "))

    DecreaPattern(value)

if __name__ == "__main__":
    main()
