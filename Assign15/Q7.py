# Write a lambda function using filter() which accepts list of string
# and returns list of string having length greater than 5

String = lambda s : len(s) >= 5

def main():
    strings = list(input("Enter list of string: ").split())

    result = list(filter(String,strings))

    print("List of strings having length is greater than 5: ", result)

if __name__ == "__main__":
    main()