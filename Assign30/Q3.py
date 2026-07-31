import schedule
import time

def task():
    print("Coding Kar...")

def main():
    schedule.every(30).minutes.do(task)

    print("Schedular started . Press Ctrl + C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()