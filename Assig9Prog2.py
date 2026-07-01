def ChkGreater(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    Value1 = int(input("Enter First Number:"))
    Value2 = int(input("Enter Second Number:"))

    Ret = ChkGreater(Value1, Value2)

    print("Greater Number is: ", Ret)

if __name__ == "__main__":
    main()