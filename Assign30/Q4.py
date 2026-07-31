import schedule
import time

def task():
    print("Namskar...")

def main():
    schedule.every().day.at("09:00").do(task)

    print("Schedular started . Press Ctrl + C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()