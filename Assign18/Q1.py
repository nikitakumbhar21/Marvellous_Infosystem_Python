# Write a program which accepts N numbers from user and store it into  List.
# Return addition of all elements from that list.

def AddElements(DataList):
    Sum = 0 

    for ele in DataList:
        Sum = Sum + ele 

    return Sum   

def main():
    size = int(input("Number of elements:"))
    elements = list(map(int,input("Input elements: ").split()))

    if len(elements) != size:
        print("Error: Number of inputs does not match the specified size.")
        return
    
    Ret = AddElements(elements)

    print(f"Addition of all elements is : {Ret}")

if __name__ == "__main__":
    main()
