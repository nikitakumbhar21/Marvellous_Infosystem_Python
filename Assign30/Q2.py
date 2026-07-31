import schedule
import time
from datetime import datetime

def display_datetime():
    now = datetime.now()
    formatted_time = now.strftime("%d-%m-%Y %I:%M:%S %p")
    print(f"Current Date and Time: {formatted_time}")

def main():
    schedule.every(1).minutes.do(display_datetime)

    print("Schedular started. Press Ctrl + C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main() 