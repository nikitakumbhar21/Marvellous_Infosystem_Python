def main():
    No = int(input("Enter Number: "))

    print("All Even numbers till ",No,"are: ")

    for i in range(2,No + 1, 2):    
        print(i, end = " ")

if __name__ == "__main__":
    main()