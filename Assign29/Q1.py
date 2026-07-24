# Check fle exists in current direcory
import os

def ChkFileExst(filename):
    if os.path.isfile(filename):
        print(f"file '{filename}' exists in the current directory")
    else:
        print(f"File '{filename}' does not exists in the current directory")

def main():
    filename = input("Enetr filename: ").strip()
    ChkFileExst(filename)

if __name__ == "__main__":
    main()