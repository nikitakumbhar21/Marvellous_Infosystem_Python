# Write a lambda function using filter() which accepts list of numbers
# and returns count of even numbers

Number = lambda a : a % 2 == 0

def main():
    no = list(map(int,input("Enter list of numbers: ").split()))

    CountEven = len(list(filter(Number,no)))

    print("Count of even numbers from list: ", CountEven)

if __name__ == "__main__":
    main()