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

def whichday(day,v,contwr):

    year = int(v)
    #print(year)
    date = int(day)
    #print(date)
    month = int(contwr)
    if month ==1:
        month = 13
        year -= 1
    elif month ==2:
        month = 14
        year -= 1
    #print(month)
    #N = d + 2m + [3(m+1)/5] + y + [y/4] - [y/100] + [y/400] +2
    n1 = int(date + 2*month + year + 2)
    #print(n1)
    n2 = int(((3*(month+1))-((3*(month+1))%5))/5)
    #print(n2)
    n3 = int((year-(year%4))/4)
    #print(n3)
    n4 = int((year-(year%100))/100)
    n5 = int((year-(year%400))/400)
    dayis = n1+n2+n3-n4+n5
    print(dayis)
    if (dayis%7) ==1:
        return('sunday')
    elif (dayis%7) ==2:
        return('monday')
    elif (dayis%7) ==3:
        return('tuesday')
    elif (dayis%7) ==4:
        return('wednesday')
    elif (dayis%7) ==5:
        return('thursday')
    elif (dayis%7) ==6:
        return('friday')
    elif (dayis%7) ==0:
        return('saturday')




leapdays = [31,29,31,30,31,30,31,31,30,31,30,31]
nonleapdays = [31,28,31,30,31,30,31,31,30,31,30,31]
start = 1900
end = fin.readline()
output = {"monday":0,
          "tuesday":0,
          "wednesday":0,
          "thursday":0,
          "friday":0,
          "saturday":0,
          "sunday":0}

for v in range(start, start + int(end)+1):
    if checkIfLeapYear(v):
        months = leapdays
    else:
        months = nonleapdays

    for month in months:
        for day in range(1,month+1):
            if day ==13:
                dayitis = whichday(day,v,month)
                output[dayitis] += 1

print(output)








