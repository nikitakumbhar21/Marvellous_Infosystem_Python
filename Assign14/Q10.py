# Write lambda function which accpets three numbers and return lrgest numbers

LargestNum = lambda a,b,c : a if a >= b and a >= c else (b if b >= c  else c)

def main():
    no1 = int(input("Enter number: "))
    no2 = int(input("Enter number: "))
    no3 = int(input("Enter number: "))

    result = LargestNum(no1,no2,no3)
    print("Largest number is: ",result)

if __name__ == "__main__":
    main()