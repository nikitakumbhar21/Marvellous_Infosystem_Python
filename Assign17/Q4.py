# write a program which accept one number from user and return addition of its factors.

def FactorAdd(No):
    Sum = 0
    for i in range(1, (No // 2) + 1):
        if No % i == 0:
            Sum = Sum + i
    return Sum
    

def main():
    value = int(input("Enter number: "))

    result = FactorAdd(value)

    print(f"Addition of {value}'s factors are:{result}")

if __name__ == "__main__":
    main()