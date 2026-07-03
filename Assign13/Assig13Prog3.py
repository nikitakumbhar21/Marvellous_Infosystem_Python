#   Check Perfect Number or not

def main():
    number = int(input("Enter a number: "))

    Sum = 0

    # Find proper divisor (from 1 up to number // 2)
    for i in range(1,(number // 2) + 1):
        if(number % 1 == 0):
            Sum = Sum + i

    # Check if the sum of divisor equals to original number
    if(Sum == number and number > 0):
        print(number,"is a Perfect Number")
    else:
        print(number,"is not Perfect Number")

if __name__ == "__main__":
    main()