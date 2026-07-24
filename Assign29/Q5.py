# Frequency of a string in File

import os

def string_frequency(filename, target_str):
    if not os.path.exists(filename):
        print(f"Error: Source file '{filename}' does not exist.")
        return
    
    try:
        file = open(filename,'r')
        content= file.read()
        # COunt full exact string occurences across the file content
        count = content.count(target_str)
        print(f"The String {target_str} appears {count} times in {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    user_input  = input("Enter file name and serach string (e.g. Demo.txt Nikita): ").split()
    if len(user_input) == 2:
        string_frequency(user_input[0],user_input[1])
    else:
        print("Please provide both a file name and string t search")

if __name__ == "__main__":
    main()