# write a program which accepts number from user and check whether that number is positive or negative 

def CheckNum(No):
    if( No > 0):
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    value = int(input("Enter Number: "))

    CheckNum(value)

if __name__ == "__main__":
    main() 
