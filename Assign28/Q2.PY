import os

def main():
    filename = input("Enter the file name: ").strip()

    if os.path.exists(filename):   # file already exists
        print(f"File {filename} already exists. \nOpening for reading...")

        try:
            fobj = open(filename, "r")   # safe context manager
            content = fobj.read()
            words = content.split()   # split handles spaces, tabs, newlines
            print(f"Total number of words in {filename}: {len(words)}")

        except Exception as err:
            print(f"An error occurred while reading: {err}")

    else:   # file does not exist
        print(f"File {filename} does not exist. Creating new file...")

        try:
            fobj= open(filename, "w")
            fobj.write("Hello, this is a new file.\n")
            print(f"File {filename} created and initialized.")

        except Exception as err:
            print(f"An error occurred while creating: {err}")

        fobj.close()

if __name__ == "__main__":
    main()
