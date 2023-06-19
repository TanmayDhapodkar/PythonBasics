#datetime.date
#Access to Year Month Date Weekday IsoWeekday

import datetime #module datetime

d = datetime.date(2023, 6, 10)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year) #Get year of today
print(tday.day) #Get day of today
print(tday.weekday()) #Monday is 0 and Sunday is 6
print(tday.isoweekday()) #Monday is 1 and Sunday is 7

#Timedeltas

tdelta = datetime.timedelta(days=7) # 7 days shift to the date

print(tday + tdelta) #print 7 days plus to the date
print(tday - tdelta) #print 7 days minus to the date

#date2 = date1 + timedelta
#timedelta = date1 + date2

bday = datetime.date(2023, 9, 13)
till_bday = bday - tday

print(till_bday) #gives today time required from current date
print(till_bday.days) #gives number of days from current date
print(till_bday.total_seconds()) #total seconds to bday

#datetime.time
#Hours Minutes Seconds Microseconds used in time

t = datetime.time(23, 45, 32, 112333)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

#datetime.datetime
#access to date and time 

dt = datetime.datetime(2023, 6, 14, 3, 4, 56, 125443)
print(dt)
print(dt.date()) #date method to extract date from datetime
print(dt.time()) #time method to extract time from datetime
print(dt.year) #year attribute to extract year from datetime
print(dt.month) #month attribute to extract month from datetime
print(dt.hour) #hour attribute to extract hour from datetime

#timedelta used in datetime

tdelta = datetime.timedelta(days=10) 
print(dt)
print(dt + tdelta)
print(dt - tdelta)

tdelta = datetime.timedelta(hours=23)
print(dt)
print(dt + tdelta)
print(dt - tdelta)

tdelta = datetime.timedelta(seconds=23)
print(dt)
print(dt + tdelta)
print(dt - tdelta)

#timezone in datetime

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
