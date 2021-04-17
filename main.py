import smtplib
import sys
from datetime import datetime
from random import randint, choice
sys.path.append('/Users/alan/')
from secret import *


today = datetime.now()

with open("birthdays.csv", "r") as birthday_file:
    birthdays = birthday_file.readlines()

    birthdays.pop(0)
    for birthday in birthdays:
        info = birthday.split(',')
        if today.day == int(info[4]) and today.month == int(info[3]):
            letter_no = randint(1,3)
            filename = f"letter_templates/letter_{letter_no}.txt"
            with open(filename, 'r') as letter:
                message = letter.read()
                message = message.replace('[NAME]', info[0])
            print(birthday)
            print(f"{GMUSER}: {GMPASS}")

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(
                    user=GMUSER,
                    password=GMPASS
                )

                smtp.sendmail(
                    from_addr=GMUSER,
                    to_addrs=info[1],
                    msg="Subject:My test subject line\n\n"
                        f"{message}"
                        "\n\nL\n\n"
                )






