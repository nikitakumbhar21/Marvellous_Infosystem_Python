# Design authomation script which accept  process name and display information of that process if its running.
# Usage : ProcInfo.py Notepad

import sys
import psutil

def is_process_runing(target_name):
    """ Check if a specific process is running and return its info"""
    matching_process = []

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            info = proc.info
            # Case-insensitive comparison
            if info['name'] and target_name.lower() in info['name'].lower():
                matching_process.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return matching_process

def display_results(process_name, matches):
    """ Display search result"""
    if matches:
        print(f"Process '{process_name}' is currently running:\n")
        print(f"{'PID':<10} {'Name':<25} {'Username':<20}")
        print("=" * 60)
        for p in matches:
            pid = p.get('pid', 'N/A')
            name = p.get('name') or 'N/A'
            username = p.get('username') or 'N/A'
            print(f"{pid:<10} {name:<25} {username:<20}")
    else:
        print(f"Process '{process_name}' is NOT running")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ProcInfo.py <ProcessName>")
        sys.exit(1)

    target_process = sys.argv[1]

    try:
        result = is_process_runing(target_process)
        display_results(target_process, result)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()