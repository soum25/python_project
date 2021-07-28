from smtplib import *
import datetime as dt
import random

now_time = dt.datetime.now()
current_day = now_time.weekday()
print(current_day)

with open("quotes.txt", "r") as quotes_files:
    data = quotes_files.readlines()
    length_data = len(data)
    for number in range(length_data):
        quotes_today = random.choice(data)
    print(quotes_today)

my_email = "vafemorymeister@gmail.com"
with SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password="Sv3maman@,")
    connection.sendmail(from_addr=my_email, to_addrs="vafesoumahoro@gmail.com",
                        msg=f"Subject:Day of week\n\n{quotes_today}")
