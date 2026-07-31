# Create New Log file Every 10 minutes

import schedule
import time
from datetime import datetime

def create_log_file():
    now = datetime.now()
    file_timestamp = now.strftime("%d_%m_%Y_%H_%M_%S")
    display_timestamp = now.strftime("%d-%m-%Y %I:%M:%S %p")

    filename = f"MarvellousLog_{file_timestamp}.txt"
    content = f"Log filr created successfully.\nCreation Time: {display_timestamp}\n"

    try:
        with open(filename,"w") as file:
            file.write(content)
        print(f"Created file: {filename}")
    except Exception as e:
        print(f"Failed to create log file: {e}")

def main():
    schedule.every(10).minutes.do(create_log_file)

    # RUn once immediately
    create_log_file()

    print("Log file creator running. Press Ctrl+C to exit")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()