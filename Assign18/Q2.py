# Write a program which accepts N numbers from user and store it into  List.
# Return Maximum number from that list.

def MaxElements(DataList):
    return max(DataList)

def main():
    size = int(input("Number of elements:"))
    elements = list(map(int,input("Input elements: ").split()))

    if len(elements) != size:
        print("Error: Number of inputs does not match the specified size.")
        return
    
    Ret = MaxElements(elements)

    print(f"Maximum number from list is : {Ret}")

if __name__ == "__main__":
    main()
