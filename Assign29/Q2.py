# Display file contents
import os

def display_content(filename):
    if not os.path.exists(filename):   # check if file does NOT exist
        print(f"File '{filename}' does not exist")
        return
    try:
        content = open(filename, 'r')   # safe context manager
        print(content.read())
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    filename = input("Enter file name: ").strip()
    display_content(filename)

if __name__ == "__main__":
    main()
