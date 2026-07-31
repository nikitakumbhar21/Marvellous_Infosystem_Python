# Count Files in Directory every 5 Minutes
# Create New Log file Every 10 minutes

import schedule
import time
import os
from datetime import datetime

def log_file_count(dir_path):
    if not os.path.exists(dir_path):
        print(f"Directory '{dir_path}' does not exist.")
        return

    try:
        file_count = sum(1 for entry in os.scandir(dir_path) if entry.is_file())
        timestamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        with open("DirectoryCountLog.txt", "a") as log:
            log.write(f"Directory path: {os.path.abspath(dir_path)}\n")
            log.write(f"Number of Files: {file_count}\n")
            log.write(f"Date and time: {timestamp}\n")
            log.write(f"-" * 40 + "\n")
        
        print(f"Loged count for {dir_path} at {timestamp}")

    except Exception as e:
        print(f"Failed to create log file: {e}")

def main():
    target_dir = input("Enter directory path: ").strip()
    
    schedule.every(5).minutes.do(log_file_count,target_dir)

    log_file_count(target_dir)

    print("File counter logger running. Press Ctrl+C to exit")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()