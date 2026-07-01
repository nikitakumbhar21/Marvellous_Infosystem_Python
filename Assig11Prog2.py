#    Count of digits
def main():
    Number = input("Enter Number: ")

    if Number.startswith('-'):
        Number = Number[1:] 

    digit_count = len(Number)
    print("Count of digits in number: ", digit_count)

if __name__ == "__main__":
    main()