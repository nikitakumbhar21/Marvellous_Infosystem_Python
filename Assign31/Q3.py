# Scan specified diectory every minute

import schedule
import time
import os
from datetime import datetime

def scan_directory(dir_path):
        if not os.path.exists(dir_path):
              print(f"directory path '{dir_path}' does not exist.")
              return
        
        file_counts = 0
        dirs_count = 0

        try:
              for entry in os.scandir(dir_path):
                    if entry.is_file(follow_symlinks=False):
                          file_counts = file_counts + 1
                    elif entry.is_dir(follow_symlinks=False):
                          dirs_count = dirs_count + 1
                
              scan_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
              print("----------------------------------")
              print(f"Directory Scanned: {os.path.abspath(dir_path)}")
              print(f"Total files: {file_counts}")
              print(f"Total Subdirectories: {dirs_count}")
              print(f"Scan Time: {scan_time}")
              print("------------------------------------")
        except Exception as e:
              print(f"Error scanning directory: {e}")

def main():
    target_dir = input("Enter directory path to scan: ").strip()
    schedule.every(1).minutes.do(scan_directory,target_dir)

    # Run once immediately
    scan_directory(target_dir)

    print("Directory scanner started. Press Ctrl+C to exit")
    while True:
          schedule.run_pending()
          time.sleep(1)

if __name__ == "__main__":
    main()