# Read and Display file contents every minutes

import os
import time

def dislay_file_contents(filepath):
    print("\n---Attempting to read file---")
    
    if not os.path.exists(filepath):
        print(f"Error: FIle does not exist.")
        return
    try:
        if os.path.getsize(filepath) == 0:
            print(f"Warning : File is empty")
            return

        f = open(filepath, "r")
        print("File Contents: ")
        print(f.read())

    except PermissionError:
        print("Error: Permission is denied.")
    except IOError:
        print("Error: File connot be opened.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")

        f.close()

def main():
    target = input("Enter the path of the file to read: ")
    print("Starting reader. Press Ctrl_C to stop.")
    while True:
        dislay_file_contents(target)
        time.sleep(60) # wait 1 minute
        
if __name__ == "__main__":
    main()