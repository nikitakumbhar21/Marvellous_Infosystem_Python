# Write a lambda function using filter() which accepts list of numbers
# and returns list of numbers divisible by 3 & 5

NumDiv5 = lambda no : (no % 3 == 0 and no % 5 == 0)

def main():
    numbers = list(map(int,input("Enter list of numbers: ").split()))

    result = list(filter(NumDiv5,numbers))

    print("List of numbers divisible by 3 & 5: ", result)

if __name__ == "__main__":
    main()