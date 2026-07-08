import threading

def SumElements(numbers,result):
    sum = 0
    if not numbers:
        return 
    for num in numbers:
        sum = sum + num
    result["sum"] = sum
    
def ProdElements(numbers,result):
    prod = 1
    if not numbers:
        return 
    for num in numbers:
        prod = prod * num
    result["prod"] = prod

def main():
    elements = list(map(int,input("Input elements: ").split()))
    
    result = {}

    t1 = threading.Thread(target= SumElements, args= (elements,result))
    t2 = threading.Thread(target= ProdElements, args= (elements,result))

    t1.start()
    t2.start()

    t1.join()  
    t2.join()

    print(f"Result form Thread 1 (Sum): {result["sum"]}")
    print(f"Result form Thread 2 (Prod): {result["prod"]}")
if __name__ == "__main__":
    main()