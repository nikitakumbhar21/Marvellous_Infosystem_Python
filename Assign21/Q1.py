import threading

def isPrime(No):
    if No < 2:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

def DisplayPrime(numbers):
    primes = []
    for num in numbers:
        if isPrime(num):
            primes.append(num)
    print(f"[Prime Thread] Prime numbers from list: {primes}")

def DisplayNonPrime(numbers):
    non_primes = []
    for num in numbers:
        if not isPrime(num):
            non_primes.append(num)
    print(f"[NonPrime Thread] Prime numbers from list: {non_primes}")

def main():
    elements = list(map(int,input("Input elements: ").split()))

    t1 = threading.Thread(target= DisplayPrime, args= (elements,), name= "Prime")
    t2 = threading.Thread(target= DisplayNonPrime, args= (elements,), name= "NonPrime")

    t1.start()
    t2.start()

    t1.join()  
    t2.join()
if __name__ == "__main__":
    main()