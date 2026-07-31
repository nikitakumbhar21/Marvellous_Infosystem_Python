# Dynamic scheduling nad system scanning
# Display message repeatedly at that interval

import schedule
import time

def display_message(msg,interval):
    print(f"{msg}\nevery {interval} seconds.\n")

def main():
    msg = input("Enter mesage").strip()
    try:
        interval = int(input("enter interval in seconds: ").strip())
        if interval <= 0:
            print("Interval must be greater than zero.")
            return
    except ValueError:
        print("Invalid number entered.")
        return
    
    schedule.every(interval).seconds.do(display_message,msg,interval)

    print("Schedular stated. Press Ctrl + C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()