import schedule
import time
from datetime import datetime

def log_timestamp():
    now = datetime.now()
    formatted_time = now.strftime("%d-%m-%Y %I:%M:%S %p")

    try:
        file = open("Marvellous.txt","a")
        file.write(f"Task executed at: {formatted_time} \n")
        print(f"Logged entry at {formatted_time}")
    except Exception as e:
        print(f"Failed to write log: {e}")

def main():
    schedule.every(5).minutes.do(log_timestamp)

    print("Schedular started . Press Ctrl + C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()