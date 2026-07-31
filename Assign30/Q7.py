import schedule
import time
import os
import shutil
from datetime import datetime

def perform_backup(source_path, dest_dir):
    if not os.path.isfile(source_path):
        print(f"Source file '{source_path}' does not exit.")
        return
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    now = datetime.now()
    timestamp_str = now.strftime("%d_%m_%Y_%H_%M_%S")
    log_time_str = now.strftime("%d-%m-%Y %I:%M:%S %p")

    base_name, ext = os.path.splitext(os.path.basename(source_path))
    backup_filename = f"{base_name}_{timestamp_str}{ext}"
    destination_file = os.athjoin(dest_dir, backup_filename)
    
    try:
        shutil.copy(source_path,destination_file)
        log_entry = f"Backup Completed Successfully at {log_time_str} -> Created {backup_filename}\n"

        log_file = open("backup_log.txt","a")
        log_file.write(log_entry)

        print(f"Backup sucessfuk: {backup_filename}")
    except Exception as e:
        print(f"Error during backup: {e}")
        
def main():
    source_file = input("Enter source file path: ").strip()
    destination_dir = input("Enter destination directory path: ").strip()

    schedule.every(1).hour.do(perform_backup, source_file, destination_dir)
    perform_backup(source_file, destination_dir)

    print("Hourly backup schedular running. Press Ctrl + C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()