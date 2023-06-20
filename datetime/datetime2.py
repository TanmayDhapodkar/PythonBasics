#timezones

import datetime
import pytz

dt = datetime.datetime(2023, 6, 20, 12, 34, 43, tzinfo=pytz.UTC) #gets dt in timezone format
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC) #current datetime in UTC
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) #current time with timezone aware
print(dt_utcnow)

#convert into different timezone
dt_utcnow1 = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow1)

dt_ind = dt_utcnow1.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_ind)

#print all timezones name list
for tz in pytz.all_timezones:
    print(tz)

#make naive datetime timezone aware
dt_local = datetime.datetime.now()
print(dt_local)

dt_east = dt_local.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

#make timezone localize
dt_utcnow1 = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow1)

mtn_tz = pytz.timezone('US/Mountain')

dt_local = mtn_tz.localize(dt_local)
print(dt_local)

dt_ind = dt_utcnow1.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_ind)

#Ways to display datetimes
dt_ind = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
print(dt_ind.isoformat()) #standard format display

print(dt_ind.strftime('%B, %d, %Y')) # %B full month in words, %d full day in numeric, %Y year in 4 digits

#Convert String into datetime
dt_str = 'June 20, 2023'
dt_convert = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt_convert)

# strftime - Convert Time to string output
# strptime - Convert String input to datetime format
