import time
import multiprocessing
import os

# Sum of fifth power fro multiple value simultaneously
def SumofFifthPower(n):
    Sum = 0

    for i in range(1,n + 1):
        Sum = Sum + (i ** 5)
    
    return Sum

def main():
    elements = list(map(int,input("Input elements: ").split()))
    
    Result = []
    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()   # create object of Pool(), 

    Result = pobj.map(SumofFifthPower,elements)  # map() function is from Pool() function (here map() is different from FMR)

    pobj.close()
    pobj.join()

    print("\nExpected Output is: ")
    print(Result)

    end_time = time.perf_counter()

    print(f"\nTotal execution time: {end_time - start_time}")


if __name__ == "__main__":
    main()
