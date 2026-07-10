import time
import multiprocessing
import os

# Sum of Even 
def SumEven(No):
    #print("Process ID : ", os.getpid())
    Sum = 0

    for i in range(2,No + 1,2):
        Sum = Sum + i
    
    return os.getpid(), No, Sum

def main():
    elements = list(map(int,input("Input elements: ").split()))
    
    Result = []

    pobj = multiprocessing.Pool()   # create object of Pool(), 

    Result = pobj.map(SumEven,elements)  # map() function is from Pool() function (here map() is different from FMR)

    pobj.close()
    pobj.join()

    print("\nExpected Output: \n")
    for pid, No, Sum in Result:
        print(f"Process Id : {pid}\nInput Number: {No}\nSum of Even Numbers:{Sum}\n")

if __name__ == "__main__":
    main()
