"""
ID: vijayaa1
LANG: PYTHON3
TASK: friday
PROG: friday
"""

#import sys

fin = open("friday.in", "r")
fout = open ('friday.out', 'w')

def checkIfLeapYear(year):
    year = int(year)
    if year%100==0:
        if year%400 ==0:
            return True
        else:
            return False
    elif year%4 == 0:
        return True
    else:
        return False

def whichday(day,v,contwer):
    def firstday(day,v,contwer):
        y = v
        d = day
        m = countwr
        firstday = d + (2*m) + ([3(m + 1) / 5]-[3(m + 1) % 5]) + y + ([y / 4]-[y%4]) - ([y / 100]-[y%100]) + ([y / 400]-[y%400]) + 2
        """
        where d is the number or the day of the month, m is the number of the 
        month, and y is the year
        """
        return(firstday)
    firstday = firstday(day,v,contwer)
    dayis = firstday
    if dayis ==1:
        return('monday')
    elif dayis ==2:
        return('tuesday')
    elif dayis ==3:
        return('wednesday')
    elif dayis ==4:
        return('thursday')
    elif dayis ==5:
        return('friday')
    elif dayis ==6:
        return('saturday')
    elif dayis ==7:
        return('sunday')



leapdays = [31,29,31,30,31,30,31,31,30,31,30,31]
nonleapdays = [31,28,31,30,31,30,31,31,30,31,30,31]
start = 1900
end = (fin.readline)
output = {"monday":0,
          "tuesday":0,
          "wednesday":0,
          "thursday":0,
          "friday":0,
          "saturday":0,
          "sunday":0}
for v in str(start),str(end):
    if checkIfLeapYear(v):
        months = leapdays
    else:
        months = nonleapdays
    countwr = 1
    for mounth in v:
        for day in months:
            if day ==13:
                print(whichday)


        countwr +=1




