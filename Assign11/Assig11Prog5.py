# Check Palindrom
def main():
    Number_str = input("Enter Number: ")

    if Number_str == Number_str[::-1]:
        print(Number_str,"is Palindrome")
    else:
        print(Number_str,"is not Palindrome")

if __name__ == "__main__":
    main()