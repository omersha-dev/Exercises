# A program to display current month in calendar view
import datetime
import calendar

today = datetime.datetime.today()

print(calendar.month(today.year, today.month))