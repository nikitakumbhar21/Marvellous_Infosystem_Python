import time
import threading

def Thread1_Display():
    print("\n--------Thread1 sequence execution started-------\n")
    print(f"[Thread1] \n")
    for i in range(1,51):
        print(i,end = " ")
        time.sleep(0.01)
    print()
        
    print("--------Thread1 sequence execution completed-------\n")

def Thread2_Display():
    print("--------Thread2 sequence execution started-------\n")
    print(f"[Thread2] \n")
    for i in range(50,0,-1):
        print(i,end = " ")
        time.sleep(0.01)
    print("\n--------Thread2 sequence execution completed-------")


def main():
    
    t1 = threading.Thread(target= Thread1_Display, name= "Thread1")
    t2 = threading.Thread(target= Thread2_Display, name= "Thread2")

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    
if __name__ == "__main__":
    main()