import time
import multiprocessing
import os

# Count Factorial of multiple numbers 
def CountFactorialNumber(No):
    print("Process ID : ", os.getpid())
    Fact = 1
    for i in range(1,No + 1):
        Fact = Fact * i
    return os.getpid(), No, Fact

def main():
    elements = list(map(int,input("Input elements: ").split()))
    
    Result = []

    pobj = multiprocessing.Pool()   # create object of Pool(), 

    Result = pobj.map(CountFactorialNumber,elements)  # map() function is from Pool() function (here map() is different from FMR)

    pobj.close()
    pobj.join()

    print("\nExpected Output: \n")
    for pid, No, count in Result:
        print(f"Process Id : {pid}\nInput Number: {No}\nCount Factorial of Number:{count}\n")

if __name__ == "__main__":
    main()
