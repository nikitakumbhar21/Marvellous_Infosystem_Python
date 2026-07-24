import os

def main():
    filename = input("Enter the source file name: ").strip()

    if os.path.exists(filename):   # file already exists
        print(f"File {filename} already exists. \nOpening for reading...")

        print(f"---------Displaying content of {filename} line by line------------")
        try:
            fobj = open(filename, "r")
            content = fobj.read()
            print(content)   # display content

            print("--------------------------------------------------------------")

            # Copy content into another file
            target_file = input("Enter the target file name to copy into: ").strip()
            copy_fobj = open(target_file, "w")
            copy_fobj.write(content)
            print(f"Content from {filename} copied successfully into {target_file}")

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

        fobj.close()

if __name__ == "__main__":
    main()
