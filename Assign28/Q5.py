import os

def main():
    filename = input("Enter the file name: ").strip()

    if os.path.exists(filename):   # file already exists
        print(f"File {filename} already exists. \nOpening for reading...")
        try:
            fobj = open(filename, "r")
            content = fobj.read()
            print(content)
            print("--------------------------------------------------------------")

            # Search for a word in the file
            search_word = input("Enter the word to search: ").strip()
            if search_word:
                if search_word in content:
                    count = content.count(search_word)
                    print(f"The word '{search_word}' was found {count} time(s) in {filename}.")
                else:
                    print(f"The word '{search_word}' was not found in {filename}.")
            else:
                print("No search word entered.")

        except Exception as err:
            print(f"An error occurred while reading: {err}")

    else:   # file does not exist
        print(f"File {filename} does not exist. Creating new file...")

        try:
            fobj = open(filename, "w")
            fobj.write("Hello, this is a new file.\n")
            print(f"File {filename} created and initialized.")
        except Exception as err:
            print(f"An error occurred while creating: {err}")

if __name__ == "__main__":
    main()
