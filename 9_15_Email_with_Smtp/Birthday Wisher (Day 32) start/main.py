from smtplib import *
import datetime as dt
import random

my_email = "vafemorymeister@gmail.com"

'''
Make the connexion secure with SMTP and starttls (Tls: transport layer security)
'''
# with SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password="Sv3maman@,")
#     connection.sendmail(from_addr=my_email, to_addrs="vafesoumahoro@gmail.com",
#                         msg="Subject:Bonjour Vafe \n\n This is the body of my email")

#
# now_time = dt.datetime.now()
# print(now_time)
# year = now_time.year
# print(year)
# print(now_time.weekday())
#
# day_of_birth = dt.datetime(year=1978, month=4, day=14)
# print(day_of_birth)

now_time = dt.datetime.now()
current_day = now_time.weekday()
print(current_day)

