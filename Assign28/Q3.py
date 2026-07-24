import os

def main():
    filename = input("Enter the file name: ").strip()

    if os.path.exists(filename):   # file already exists
        print(f"File {filename} already exists. \nOpening for reading...")

        print(f"---------Displaying content of {filename} line by line------------")
        try:
            fobj = open(filename, "r")
            for line in fobj:
                print(line,end= "")     #   end="" preventing adding an extra newline since already contains '\n'
            print("\n--------------------------------------------------------------")

        except Exception as err:
            print(f"An error occurred while reading: {err}")

    else:   # file does not exist
        print(f"File {filename} does not exist. Creating new file...")

        try:
            with open(filename, "w") as fobj:
                fobj.write("Hello, this is a new file.\n")
                print(f"File {filename} created and initialized.")

        except Exception as err:
            print(f"An error occurred while creating: {err}")
        
            fobj.close()

if __name__ == "__main__":
    main()
