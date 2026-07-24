# Compare two files(Command Line)
import os
import sys

def compare_file(file1,file2):
    if not os.path.exists(file1) or not os.path.exists(file2):
        print("File not exists")
        return
    
    try:
        f1 = open(file1,'r')
        f2 = open(file2,'r')
        if f1.read() == f2.read():
            print("Success")
        else:
            print("Failure")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python script.py <file1> <file2>")
    else:
        compare_file(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()