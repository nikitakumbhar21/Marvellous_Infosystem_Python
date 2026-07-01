#   Sum of digits
def main():
    No = input("Enter Number:")

    Sum = 0 

    for no in str(No):
        Sum = Sum + int(no) 

    print("Sum of digit is : ",Sum)
    
if __name__ == "__main__":
    main()