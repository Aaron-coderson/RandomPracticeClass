def whichday(day,v,contwr):

    year = int(v)
    day = int(day)
    month = int(contwr)
    firstday = day + (2*month) + ([3(month + 1) / 5]-[3(month + 1) % 5]) + year + ([year/ 4]-[y%4]) - ([year/ 100]-[y%100]) + ([year/ 400]-[y%400]) + 2
    """
    where d is the number or the day of the month, m is the number of the 
    month, and y is the year
    """
    dayis = firstday

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

print(whichday(23,2020,5))