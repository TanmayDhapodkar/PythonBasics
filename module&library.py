# print list of vegetables using importing module
import importmodules as im

veg = ['cabbage','carrot','onion','potato']

#Index to find a particular vegtable using importing module
index = im.findindex(veg,'potato') #find potato using module imported
print(index)

#Import the function instead of module
from importmodules import findindex

veg = ['cabbage','carrot','onion','potato']

#Index to find a particular vegtable using importing module
index = findindex(veg,'potato') #find potato using module imported
print(index)

# Import function and variable
from importmodules import findindex, test

veg = ['cabbage','carrot','onion','potato']

#Index to find a particular vegtable using importing module
index = findindex(veg,'potato') #find potato using module imported
print(index)
print(test)

# Give Alias to module with function and variable
from importmodules import findindex as im, test

veg = ['cabbage','carrot','onion','potato']

#Index to find a particular vegtable using importing module
index = im(veg,'potato') #find potato using module imported
print(index)
print(test)

#How to find a module
from importmodules import findindex as im, test
import sys

veg = ['cabbage','carrot','onion','potato']

#Index to find a particular vegtable using importing module
index = im(veg,'potato') #find potato using module imported
print(sys.path)

#Random Module
import random

veg = ['cabbage','carrot','onion','potato']
random_course = random.choice(veg) #use random module from library and get any random value from list
print (random_course)

#Math Module
import math

rads = math.radians(90)
print(rads)
print(math.sin(45))

#Import Datetime & calender
import datetime
import calendar

today = datetime.date.today() #get todays date using datetime library
print(today)
print(calendar.isleap(2023))

#Import OS
import os
print(os.getcwd())
print(os.__file__)
