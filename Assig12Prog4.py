# Print N numbers starting from 1
def main():
    no = int(input("Enter number: "))

    for i in range(1, no + 1):
        print(i, end = " ")
    print()

if __name__ == "__main__":
    main()
