# Main method

import Q5_MarvellousNum

def ListPrime(DataList):
    sum = 0

    for ele in DataList:
        if Q5_MarvellousNum.ChkPrime(ele):
            sum = sum + ele
    return sum

def main():
    size = int(input("Number of elements:"))
    elements = list(map(int,input("Input elements: ").split()))

    if len(elements) != size:
        print("Error: Number of inputs does not match the specified size.")
        return
    Ret = ListPrime(elements)

    print(f"Addition of all prime number is : {Ret}")

if __name__ == "__main__":
    main()