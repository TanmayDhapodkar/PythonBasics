#Leap Year Identifier

#Number of days per month, First Value placeholder for indexing purpose
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

"""Return True for leap years, False for Non Leap years"""

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0 )

""" Return number of days in that month in that year"""

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
        
    return month_days[month]
    
print(is_leap(2020)) # Find leap year
print(days_in_month(2099,7)) # Find days in month
