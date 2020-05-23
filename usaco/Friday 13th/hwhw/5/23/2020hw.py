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
    #N = d + 2m + [3(m+1)/5] + y + [y/4] - [y/100] + [y/400] +
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

print(whichday(2,2108,6))