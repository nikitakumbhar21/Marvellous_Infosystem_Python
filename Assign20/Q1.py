
import threading    #(used join())

#   Print first 10 Even Numbers
def Even(No):
    print("First 10 even numbers are : ", end= " ")
    for i in range(2,21,2):
        i % 2 == 0
        print(i, end= " ")
    print()


#   Print first 10 Odd Numbers
def Odd(No):
    print("First 10 odd numbers are : ", end= " ")
    for i in range(1,21,2):
        i % 2 != 0
        print(i, end= " ")
    print()

def main():

   t1 = threading.Thread(target= Even, args= (1,))
   t2 = threading.Thread(target= Odd, args= (1,))

   t1.start()
   t2.start()

   t1.join()
   t2.join()

if __name__ == "__main__":
    main()