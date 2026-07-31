# Copy .txt Files Every Ten Minutes

import os
import time
import shutil
import datetime

def copy_text_files(src,dest):
    # Validate both directories    
    if not os.path.exists(src) or not os.path.isdir(src):
        print(f"Error: Source directory is invalid or does not exist.")
        return

    if not os.path.exists(dest):
        try:
            os.makedirs(dest) # create dest if it dosen't exist
            print(f"Created destination directory: {dest}")
        except Exception as e:
            print("Error: Destination directory is invalid and cannot be created {e}.")
            return

    log_filename = "CopyOperationsLog.txt"

    log = open(log_filename,"a")
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    log.write(f"\n------Copy Opeartion started: {timestamp} ----\n")

    for filename in os.listdir(src):
        if filename.endswith(".txt"):
            src_file = os.path.join(src, filename)
            dest_file = os.path.join(dest, filename)

            # Avoid terminating if one file cannot be copied
            try:
                shutil.copy2(src_file, dest_file)
                log.write(f"SUCCESS: Copied {filename}\n")
                print(f"Copied {filename}")
            except Exception as e:
                log.write(f"FAILED: Could not copy {filename}. Error: {e}\n")
                print(f"Failed to copy {filename}")

def main():
    source_dir = input("Enter source directory path: ")
    destination_dir = input("Enter desination directory path: ")
    print("Starting reader. Press Ctrl_C to stop.")
    while True:
        copy_text_files(source_dir, destination_dir)
        time.sleep(600) # wait 10 minute
        
if __name__ == "__main__":
    main()