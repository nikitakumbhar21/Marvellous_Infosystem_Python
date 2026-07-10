import time
import multiprocessing
import os

# Count Odd numbers 
def CountOdd(No):
    print("Process ID : ", os.getpid())
    count = 0
    for i in range(1,No + 1,):
        if i % 2 != 0:
            count = count + 1    
    return os.getpid(), No, count

def main():
    elements = list(map(int,input("Input elements: ").split()))
    
    Result = []

    pobj = multiprocessing.Pool()   # create object of Pool(), 

    Result = pobj.map(CountOdd,elements)  # map() function is from Pool() function (here map() is different from FMR)

    pobj.close()
    pobj.join()

    print("\nExpected Output: \n")
    for pid, No, count in Result:
        print(f"Process Id : {pid}\nInput Number: {No}\nCount Odd Numbers:{count}\n")

if __name__ == "__main__":
    main()
