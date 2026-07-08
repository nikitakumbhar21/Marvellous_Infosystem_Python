# Write a program which display first 10 even numbers on screen.

def DisplayEven():
    no = 2
    for i in range(2,21,2):
        print(i, end =" ")
    print()

    
def main():
    print("Fisrt 10 even numbers:")
    DisplayEven()

if __name__ == "__main__":
    main()