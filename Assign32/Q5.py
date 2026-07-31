# Delete Empty Files Every hour

import os
import time
import datetime

def clean_empty_files(target_dir):
    log_filename = "DeletedEmptyFilesLog.txt"

    if not os.path.exists(target_dir) or not os.path.isdir(target_dir):
        print("Error: The specified sample directory is invalid.")
        return

    log = open(log_filename,"a")
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    log.write(f"\n---Scan Started: {timestamp} ----")

    # Scan the directory recursively
    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            filepath = os.path.join(root, filename)

            try:
                # Detect files whose size is zero bytes
                if os.path.getsize(filepath) == 0:
                    os.remove(filepath) # Delete the empty files
                    log.write(f"DELETED: {filepath}\n")
                    print(f"Deleted empty file: {filepath}")
            # Handle permisso errors
            except PermissionError:
                log.write(f"PERMISSiON ERROR: Cannot access/delete {filepath}\n")
            except Exception as e:
                log.write(f"ERROR: /Issue procesing {filepath}. details: {e}\n")

def main():
    print("WARNING: Test this program only on a sample directory.")
    target = input("Enter the path to the sample directory to clean: ")

    print("Starting cleanup schedular. Press Ctrl+C to stop.")
    while True:
        clean_empty_files(target)
        time.sleep(3600) # Wait 1 hour
if __name__ == "__main__":
    main()