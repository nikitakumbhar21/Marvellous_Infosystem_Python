# Write lambda function to return maximum of two number

MaxNo = lambda a,b : a if a > b else b

def main():
    No1 = int(input("Enter first Numbers: "))
    No2 = int(input("Enter second Numbers: "))
    
    result = MaxNo(No1,No2)
    print("Maximum of two number is", result)

if __name__ == "__main__":
    main()