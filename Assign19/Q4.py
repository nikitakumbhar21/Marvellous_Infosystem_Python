# Filter : Filter out numbers whihc are even
ChkEven =  lambda No :  No % 2 == 0

#   Mapping : Calculate its square
#   Return value : Should not boolean value
Square = lambda No : No ** 2

#   Reduce : We can do operations( Mathematical operations which is reduce to get output in single unit)
#   Return Value : Should be in two parameters
Addition = lambda No1, No2 : No1 + No2

#   User Defined Filter Function
def filterX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)  # ChkEven(No)

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

    FData = list(filterX(ChkEven, elements))   
    print("List After Filter: ", FData)

    MData = list(mapX(Square, FData))
    print("List After Mapping: ", MData)

    RData = reduceX(Addition, MData)
    print("Output of Reduce: ", RData)

    
if __name__ == "__main__":
    main()