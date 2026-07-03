#   Print N Numbers in reverse order

def main():
    number = int(input("Enter a number:"))

    for i in range(number, 0, -1):
        print(i, end = " ")
    print()

if __name__ == "__main__":
    main()