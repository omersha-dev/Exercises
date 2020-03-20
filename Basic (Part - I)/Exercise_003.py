from datetime import date, datetime

date = date.today()
time = datetime.now()

print('Date and time:\n' + date.strftime("%y/%m/%d") + ' ' + time.strftime("%H:%M:%S"))