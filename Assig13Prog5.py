# Display Grade Based on Marks

def main():
    marks = float(input("Enter marks:"))

    if marks >= 75:
        print("Grade: Distinction")
    elif marks >= 60:
        print("Grade: First Class")
    elif marks >= 50:
        print("Grade: Second Class")
    else:
        print("Grade: Fail")

if __name__ == "__main__":
    main()