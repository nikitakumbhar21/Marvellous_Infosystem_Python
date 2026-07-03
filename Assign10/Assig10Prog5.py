def main():
    No = int(input("Enter Number: "))

    print("All Odd numbers till ",No,"are: ")

    for i in range(1,No + 1, 2):
        print(i, end = " ")

if __name__ == "__main__":
    main()