# Design authomation script which display informatin of runing process as its name , PID, Username
# Usage : ProcInfo.py

import sys
import psutil

def get_process_info():
    """ Fetch information of all running processes."""
    process_list = []

    for proc in psutil.process_iter(['pid','name', 'username']):
        try:
            info = proc.info
            process_list.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return process_list

def display_processes(processes):
    """ Display process info on screen."""
    print(f"{'PID':<10} {'Name':<25} {'Username':<20}")
    print("=" * 60)
    for p in processes:
        pid = p.get('pid', 'N/A')
        name = p.get('name') or 'N/A'
        username = p.get('username') or 'N/A'
        print(f"{pid:<10} {name:<25} {username:<20}")

def main():
    try:
        processes= get_process_info()
        display_processes(processes)
    except Exception as e:
        print(f"An unexpected error ocurred: {e}")

if __name__ == "__main__":
    main()