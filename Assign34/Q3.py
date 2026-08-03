# Accept directory name from user and create log file in that directory which contains info of running processes as its name , PID, username
# Usage : ProcInfoLog.py Demo

import os
import sys
import time
import psutil

def create_directory(dir_name):
    # create directory if it's not exists.
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def generate_log_file(dir_name):
    # Generate log file containing running process information,.
    create_directory(dir_name)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(dir_name, f"Marvellous_ProcLog_{timestamp}.log")

    try:
        f = open(log_file_path, "w", encoding = "utf-8")
        f.write("\n===============================================\n")
        f.write("Process Information Log\n")
        f.write("Generated on " + time.ctime() + "\n")
        f.write("\n===============================================\n")

        #  Iterate through all running processes
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                f.write(f"Process name: {proc.info['name']}\n")
                f.write(f"PID: {proc.info['pid']}\n")
                f.write(f"User: {proc.info['username']}\n")
                f.write("------------------------------------------\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        print(f"Log file created successfully at: {log_file_path}")
    except Exception as e:
        print(f"Error while reatng log fle: {e}")

        f.close()

def main():
    if len(sys.argv) != 2:
        print("Usage: ProcInfoLog.py <DirectoryName>")
        return

    dir_name = sys.argv[1]
    generate_log_file(dir_name)

if __name__ == "__main__":
    main()