# Filter : Filter out numbers wuch greater than or equal to 70 and less than or equal to 90
GreaterNum =  lambda No :  70 <= No <= 90

#   Mapping : Increment no by 10 (No+10)
#   Return value : Should not boolean value
IncreaseNum = lambda No : No + 10

#   Reduce : We can do operations( Mathematical operations which is reduce to get output in single unit)
#   Return Value : Should be in two parameters
ProdNum = lambda No1, No2 : No1 * No2

#   User Defined Filter Function
def filterX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)  # GreaterNum(No)

        if(Ret == True):
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)  # IncreaseNum(No)
        Result.append(Ret)

    return Result

def reduceX(Task, Elements):
    Prod = 1

    for no in Elements:
        Prod = Task(Prod,no)  # ProdNum(No1,No2)

    return Prod

def main():
    elements = list(map(int,input("Input List: ").split()))

    FData = list(filterX(GreaterNum, elements))   
    print("List After Filter: ", FData)

    MData = list(mapX(IncreaseNum, FData))
    print("List After Mapping: ", MData)

    RData = reduceX(ProdNum, MData)
    print("Output of Reduce: ", RData)

    
if __name__ == "__main__":
    main()