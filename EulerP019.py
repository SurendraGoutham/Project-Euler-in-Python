'''
Created on 28-Nov-2013

@author: 00003179



You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''
import calendar

count = 0
countSundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if(calendar.weekday(year, month, 1) == 6):  # here 6 means Sunday and 1 means 1st day of the month - calendar date function wise
            # print "Year", year , "Month" , month
            count += 1
        # Code for calculating number of Sundays in twentieth century (1 Jan 1901 to 31 Dec 2000)
        for day in range(1,32):
            try:
                if(calendar.weekday(year, month, day) == 6):
                    countSundays += 1
            except:
                pass

print countSundays, "Sundays in the twentieth century (1 Jan 1901 to 31 Dec 2000)"
print count, "Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)"
