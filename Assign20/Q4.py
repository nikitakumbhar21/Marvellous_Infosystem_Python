
import threading   

def CountSmall(string):
    current_thread = threading.current_thread()
    small = []
    for i in string:
        if i.islower():
            small.append(i)
        
    print(f"Thread Name: {current_thread.name} | Thread ID: {current_thread.ident} ")
    print(f"Number of lowercase characters: {len(small)}")
    print()

def CountCapital(string):
    current_thread = threading.current_thread()
    capital = []
    for i in string:
        if i.isupper():
            capital.append(i)
        
    print(f"Thread Name: {current_thread.name} | Thread ID: {current_thread.ident} ")
    print(f"Number of capital characters: {len(capital)}")
    print()

def CountDigits(string):
    current_thread = threading.current_thread()
    digit = []
    for i in string:
        if i.isdigit():
            digit.append(i)
        
    print(f"Thread Name: {current_thread.name} | Thread ID: {current_thread.ident} ")
    print(f"Number of numeric digits: {len(digit)}")
    print()

def main():
    strinput = input("Enter string: ")
    
    t1 = threading.Thread(target= CountSmall, args= (strinput,), name= "Small")
    t2 = threading.Thread(target= CountCapital, args= (strinput,),  name= "Capital")
    t3 = threading.Thread(target= CountDigits, args= (strinput,),  name= "Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    
if __name__ == "__main__":
    main()