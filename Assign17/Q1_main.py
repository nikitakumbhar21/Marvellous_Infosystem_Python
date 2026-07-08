# main method

from Q1_Arithmetic import Add, Sub, Mult, Div

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    Addition = Add(value1, value2)
    print(f"Addition is: {Addition}")

    Substraction = Sub(value1, value2)
    print(f"Substraction is: {Substraction}")

    Multiplication = Mult(value1, value2)
    print(f"Multiplication is: {Multiplication}")

    Division = Div(value1, value2)
    print(f"Division is: {Division}")

if __name__ == "__main__":
    main()

