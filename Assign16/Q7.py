# Write a program which conatins one function that accept one number from user 
# and returns true if number is divisible by 5 otherwise retuns false.

def DivBy(No):
    if No % 5 == 0:
        return True
    else:
        return False
    
def main():
    value = int(input("Enter number: "))

    Ret = DivBy(value)

    print(Ret)

if __name__ == "__main__":
    main()