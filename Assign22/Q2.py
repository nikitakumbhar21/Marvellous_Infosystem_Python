import time
import multiprocessing
import os
import math

# Factorial Of Multiple Numbers
def FactorialOfNumbers(num):
    '''
    # Return atuple containing (Process ID, Input Number, Result)
    return os.getpid(), No, math.factorial(No)
    '''

    #print("Process is running with PID : ", os.getpid())
    Fact = 1
    for i in range(1,num + 1):
        Fact = Fact * i
    return os.getpid(), num, Fact
    

def main():
    elements = list(map(int,input("Input numbers: ").split()))
    
    Result = []

    pobj = multiprocessing.Pool()   # create object of Pool(), 

    Result = pool.map(FactorialOfNumbers,elements)  # map() function is from Pool() function (here map() is different from FMR)
    
    pobj.close()
    pobj.join()

    print("\nFactorial of each numbers are: ")
    for pid, num, Fact in Result:
        print(f"Process ID: {pid} | Input Number: {num} | Factorial : {Fact}")

if __name__ == "__main__":
    main()
