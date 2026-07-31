# Monitor file size every 30 seconds

import os
import time
import datetime

def monitor_file(filepath):
    log_file = "FileSizeLog.txt"
    now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    log = open(log_file,"a")
    if not os.path.exists(filepath):
        log.write(f"File path/; {filepath} | Error: File does not exist | date and time: {now}\n")
        print(f"Logged missing file state at {now}")
    else:
        size = os.path.getsize(filepath)
        log.write(f"File path: {filepath} | File size in bytes: {size} | Date and time: {now}\n")
        print(f"Logged file size({size} bytes) at {now}")

    log.close()

def main():
    target_file = input("Enter the path of the file to monitor: ")
    print("Starting monitoring. Press Ctrl_C to stop.")
    while True:
        monitor_file(target_file)
        time.sleep(30) # wait 30 seconds

if __name__ == "__main__":
    main()