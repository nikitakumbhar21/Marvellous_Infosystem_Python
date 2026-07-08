import threading

def MaxElements(numbers):
    if not numbers:
        return 
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    print(f"[Thread1] Maximum element is: {max_val}")

def MinElements(numbers):
    if not numbers:
        return 
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    print(f"[Thread1] Minimum element is: {min_val}")
def main():
    elements = list(map(int,input("Input elements: ").split()))
    t1 = threading.Thread(target= MaxElements, args= (elements,), name= "Thread1")
    t2 = threading.Thread(target= MinElements, args= (elements,), name= "Thread2")

    t1.start()
    t2.start()

    t1.join()  
    t2.join()
if __name__ == "__main__":
    main()