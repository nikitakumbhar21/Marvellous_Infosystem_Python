# Write a program which contains one function named as  ChkNum() which accept one parameter as number.
# If num is evem then it should print display "Even number" otherwise display "Odd number" on console.

def ChkNum(number):
    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
    
def main():
    No = int(input("Enter Number: "))

    ChkNum(No)

if __name__ == "__main__":
    main()

