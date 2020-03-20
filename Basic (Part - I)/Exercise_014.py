from datetime import date
firstDate = date(2014, 7, 2)
lastDate = date( 2014, 10, 5)
deltaDate = lastDate - firstDate
print(deltaDate.days)