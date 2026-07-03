# Reverse of number
def main():
    Number_str = input("Enter Number:")

    if Number_str.startswith('-'):          #   Check if the number is negative to maintain the sign position
        reverse_str = '-' + Number_str[1:][::-1]
    else:
        reverse_str = Number_str[::-1]
    print("Reversed Number: ", reverse_str)

if __name__ == "__main__":
    main()