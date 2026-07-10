import time
import multiprocessing
import os

# Sum of Square
def SumSquare(No):
    #print("Process is running with PID : ", os.getpid())
    Sum = 0

    for i in range(1,No + 1):
        Sum = Sum + (i ** 2)
    
    return Sum

def main():
    elements = list(map(int,input("Input elements: ").split()))
    
    Result = []

    pobj = multiprocessing.Pool()   # create object of Pool(), 

    Result = pobj.map(SumSquare,elements)  # map() function is from Pool() function (here map() is different from FMR)

    pobj.close()
    pobj.join()

    print("\nExpected Output is: ")
    print(Result)

if __name__ == "__main__":
    main()
