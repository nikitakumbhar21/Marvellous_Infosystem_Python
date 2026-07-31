import schedule
import time

def task():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(task)

    print("Schedular started . Press Ctrl + C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()