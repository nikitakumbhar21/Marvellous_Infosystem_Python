# Schedule weekly Messages using schedule
# Requires the schedule library: pip install schedule

import time
import schedule

def job_monday():
    print("Start your weekly goals")

def job_wednesday():
    print("Review your weekly progress")

def job_friday():
    print("Weekly work completed")

def main():

    # Scheduling the tasks
    schedule.every().monday.at("09:00").do(job_monday)
    schedule.every().wednesday.at("17:00").do(job_wednesday)
    schedule.every().friday.at("18:00").do(job_friday)

    print("Schedular started. Press Ctrl+C to exit...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()