# Write a program which accepts number from user 
# and print that number of "*" on screen.


#first approach: 

def PrintStarts(No):
    for i in range(No):
        print("* ", end = " ")
    print()

def main():
    value = int(input("Enter number: "))
    #print("* "*value)   # another approach

    PrintStarts(value)
   
if __name__ == "__main__":
    main()