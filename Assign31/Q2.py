# Schedule task with function arguments

import schedule
import time

def DisplayMessage(message):
    print(f"Message: {message}")

def main():
    msg = input("Enter the mesaage to display: ").strip()
    schedule.every(5).seconds.do(DisplayMessage, msg)
    print("Schedulary started . Press Ctrl+C to exit")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()