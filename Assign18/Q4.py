# Write a program which accepts N numbers from user and store it into  List.
# Accept one another number form user and return frequency of that number from list
def CalFrequency(DataList, Target):
    count = 0
    for ele in DataList:
        if ele == Target:
            count = count + 1
    return count

def main():
    size = int(input("Number of elements:"))
    elements = list(map(int,input("Input elements: ").split()))

    if len(elements) != size:
        print("Error: Number of inputs does not match the specified size.")
        return
    search_elements = int(input("Enter number to search: "))
    Ret = CalFrequency(elements, search_elements)

    print(f"Frequency of number is : {Ret}")

if __name__ == "__main__":
    main()
