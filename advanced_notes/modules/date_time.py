import datetime

date = datetime.date(1999, 4, 20)
today = datetime.date.today()

time = datetime.time(5, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")

target_datetime = datetime.datetime(2030, 4, 20, 12, 0, 0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has already passed!")
else:
    print("Target date has NOT passed!")