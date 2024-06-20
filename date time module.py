""" in date time module we can import the date and
time seperately as well as combined"""
import datetime as dt
d = dt.datetime.now()
print(d)
print(d.year)
#by using this function strftime we can format the date an time
print(d.strftime("%A"))
print(d.strftime("%a"))
print(d.strftime("%B"))
print(d.strftime("%b"))
      
from datetime import date
y = datetime.datetime(2024,6,13)
print(y)
#this program print the date with the daays starting time as 00.00.00
