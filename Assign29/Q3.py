# Copy file contents into new file (command line)
import os
import sys

def copy_to_demo(source_file):
    target_file = "CopyDemo.txt"

    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' does not exist.")
        return
    
    try:
        src = open(source_file,'r')
        dest = open(target_file,'w')
        dest.write(src.read())
        print(f"Created {target_file} and copied contents of {source_file} into {target_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python script.py <Source_File>")
    else:
        copy_to_demo(sys.argv[1])

if __name__ == "__main__":
    main()