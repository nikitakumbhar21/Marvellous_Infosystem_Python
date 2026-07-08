def ChkPrime(No):
    if No < 2:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

#   Mapping : Calculate its square
#   Return value : Should not boolean value
Mult = lambda No : No * 2

#   Reduce : We can do operations( Mathematical operations which is reduce to get output in single unit)
#   Return Value : Should be in two parameters
MaxNum = lambda No1, No2 : No1 if No1 > No2 else No2

#   User Defined Filter Function
def filterX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)  # ChkPrime(No)

        if(Ret == True):
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)  # Square(No)
        Result.append(Ret)

    return Result

def reduceX(Task, Elements):
    Sum = 0

    for no in Elements:
        Sum = Task(Sum,no)  # Addition(No1,No2)

    return Sum

def main():
    elements = list(map(int,input("Input elements: ").split()))

    FData = list(filterX(ChkPrime, elements))   
    print("List After Filter: ", FData)

    MData = list(mapX(Mult, FData))
    print("List After Mapping: ", MData)

    RData = reduceX(MaxNum, MData)
    print("Output of Reduce: ", RData)

    
if __name__ == "__main__":
    main()