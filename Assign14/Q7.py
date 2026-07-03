# Write lambda function which returns True if divisible by 5

DivBy = lambda a : True if a % 5 == 0 else False

def main():
    no = int(input("Enter number: "))

    result = DivBy(no)
    print(result)

if __name__ == "__main__":
    main()