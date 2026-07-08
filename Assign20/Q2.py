
import threading 

def EvenFactor(number):
    factors = []
    for i in range(1,number+1):
        if number % i == 0 and i % 2 == 0:
            factors.append(i)
        
    print(f"Even factor of {number}: {factors} ")
    print(f"Sum of even factors: {sum(factors)}")

def OddFactor(number):
    factors = []
    for i in range(1,number+1):
        if number % i == 0 and i % 2 != 0:
            factors.append(i)
        
    print(f"Odd factor of {number}: {factors} ")
    print(f"Sum of odd factors: {sum(factors)}")

def main():
    num = int(input("Enter an integer number: "))
    
    t1 = threading.Thread(target= EvenFactor, args= (num,))
    t2 = threading.Thread(target= OddFactor, args= (num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")
if __name__ == "__main__":
    main()