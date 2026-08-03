# Log Process Info and email file
# usage: python ProcInfoLogpy Demo Marvellousinfosystem@gmail.com

import os
import sys
import time
import re
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import psutil

# Configuration for  mail server
sender_email = "kumbharniki21.nk@gmail.com"
sender_password = "anikAnand#p00" 

# Email validation
def validate_email(email):
    # Validate email address format
    pattern = r'[a-zA-Z0-9._%+-] + @[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email)

#Log file creation
def create_log_fle(dir_name):
    # create directory if it's not exists.
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        filename = f"Proces_Log_{time.strftime("%Y%m%d_%H%M%S")}.log"
        file_path = os.path.join(dir_name, filename)

        f = open(file_path,"w", encoding="utf-8")
        f.write(f"Proess Information Log - {time.ctime()}\n")
        f.write("="* 65 + "\n\n")
        f.write(f"{'PID':<10} {'Name':<30} {'Username:<25'}")
        f.write("="* 65 + "\n")

        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                pinfo = proc.info
                pid = pinfo.get('pid', 'N/A')
                name = pinfo.get('name') or 'N/A'
                username = pinfo.get('sername') or 'N/A'
                f.write(f"{pid<10} {name:<30} {username:<25}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        return file_path

def send_email(to_email, file_path):
    # Send log file as attachment via email
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = f"Proces Log Reports - {time.ctime()}"

        body = "Hello,\n\n Please find the attached system process logfile.\n\nBest Regards,\nAutomation Scripts"
        msg.attach(MIMEText(body,'plain'))

        # Attached file
        attachment = open(file_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachement; filename= {os.path.basename(file_path)}")
        msg.attach(part)

        # COnnect to Gmail SMPT server
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(sender_email,sender_password)
        smtp.send_message(msg)
        smtp.quit()

        print(f"Log file sucessfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

        attachment.close()

def main():
    if len(sys.argv) != 3:
        print("Usage: python PocInfoLog.py <DirectoryName> <EmailID>")
        sys.exit(1)

    dir_name = sys.argv[1]
    recipient_email = sys.argv[2]

    
    try:
        print("Generating process log...")
        log_path = create_log_fle(dir_name)
        print(f"Log saved at: {log_path}")

        print("Sending mail...")
        send_email(recipient_email, log_path)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
