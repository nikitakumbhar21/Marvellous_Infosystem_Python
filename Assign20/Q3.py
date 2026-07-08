
import threading

def EvenList(number):
    even = []
    for i in number:
        if i % 2 == 0:
            even.append(i)
        
    print(f"Extracted even elements: {even} ")
    print(f"Sum of extracted even elelments: {sum(even)}")
    print()

def OddList(number):
    odd = []
    for i in number:
        if i % 2 != 0:
            odd.append(i)
        
    print(f"Extracted odd elements: {odd} ")
    print(f"Sum of extracted odd elelments: {sum(odd)}")
    print()

def main():
    elements = list(map(int,input("Input elements: ").split()))

    
    t1 = threading.Thread(target= EvenList, args= (elements,))
    t2 = threading.Thread(target= OddList, args= (elements,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
if __name__ == "__main__":
    main()