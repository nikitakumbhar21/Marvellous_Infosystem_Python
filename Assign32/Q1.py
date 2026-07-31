# Create a New text file every minutes

import datetime
import time

def create_timestamped_file():
    now = datetime.datetime.now()

    #Format: File_DD_MM_YY_HH_MM_SS.txt
    filename = now.strftime("File_%d_%m_%Y_%H_%M_%S.txt")

    date_str = now.strftime("%d-%m-%Y")
    time_str = now.strftime("%H:%M:%S")

    f = open(filename,"w")
    f.write(f"Filename: {filename}\n")
    f.write(f"Creation date: {date_str}\n")
    f.write(f"Creation time: {time_str}\n")

    print(f"Successfully created: {filename}")

    f.close()

def main():
    print("starting script. Press Ctrl+C to stop")
    while True:
        create_timestamped_file()
        time.sleep(60) #wait 1 minute

if __name__ == "__main__":
    main()
