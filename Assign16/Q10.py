# Write a program which accepts name from user and display length of its name.

def DisplayName(name):
    lenName = len(name)
    return lenName

    
def main():
    user_name = input("Enter name: ")
    result = DisplayName(user_name)

    print(f"Length of given name is: {result}")

if __name__ == "__main__":
    main()