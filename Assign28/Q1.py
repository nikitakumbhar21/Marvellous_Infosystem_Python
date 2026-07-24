import os

def main():
    filename = input("Enter the file name: ").strip()

    if os.path.exists(filename):
        print(f"Error: File {filename} does not exist")
        return
    else:
        fobj = open("Demo.txt","w")
        print("File gets open")
        fobj.write("Hello My name is Nikita\n I am 29 years old\n I'm having cute little baby girl\n and Her name is Kishori\n Kishori name is divine of Radharani\n So we call her Radha as nickname")
        try:
            fobj = open(filename, "r") 
            lines = fobj.readlines()
            print(f"Total number of lines in {filename}: {len(lines)}")
        except FileNotFoundError as fobj:
            print(f"An error ocuured: {fobj}")
        
        fobj.close()

if __name__ == "__main__":
    main()
