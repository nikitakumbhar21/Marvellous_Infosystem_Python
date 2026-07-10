import time
import multiprocessing
import os
import math

# Helper Function to check if single number is prime.........̣.,j.jjlk
def IsPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Count Prime 1 to N
def CountPrime(n):
    # Count how many primes exist from 1 to N
    count = 0
    for i in range(1, n + 1):
        if IsPrime(i):
            count = count + 1
    # Return the process Id, input number and total count
    return os.getpid(), n, count


def main():
    elements = list(map(int,input("Input numbers: ").split()))
    
    Result = []
    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()   # create object of Pool(), 

    Result = pobj.map(CountPrime,elements)  # map() function is from Pool() function (here map() is different from FMR)
    
    pobj.close()
    pobj.join()
    
    print("\nPrime numbers form 1 to N: ")
    print()
    for pid,num,count in Result:
        print(f"Process ID: {pid} | Input Number: {num} | Prime Count : {count}")

    end_time = time.perf_counter()

    print(f"Total execution time: {end_time - start_time}")

if __name__ == "__main__":
    main()
