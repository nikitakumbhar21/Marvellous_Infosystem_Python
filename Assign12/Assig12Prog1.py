# Check Vowel or Consonant

def main():
    char = input("Enter a character: ")

    char_lower = char.lower()                   #   Convert to lowercase to handle both uppper and lower case inputs

    if len(char_lower) == 1 and char_lower.isalpha():       #   Check if the input is a single alphabetic charatcter
        if char_lower in ['a','e','i','o','u']:
            print(char_lower,"is Vowel")
        else:
            print(char_lower,"is Consonent")
    else:
        print("Please enter a single valid letter")

if __name__ == "__main__":
    main()