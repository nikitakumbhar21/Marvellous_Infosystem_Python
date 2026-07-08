# Write a program which display 10 to 1 on screen

def display():
    for i in range(10,0,-1):
        print(i, end= " ")
    print()

if __name__ == "__main__":
    display()