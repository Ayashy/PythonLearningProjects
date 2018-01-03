

import sys



def solve(year):
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    days=256
    if 1700 <= year <=1917:
        #Julian
        if year%4==0 :
            months[1]=29
        for index,month in enumerate(months):
            if days<=month :
                return '{:02}.{:02}.{:02} '.format(days,index+1,year)
            else:
                days-=month
    elif year==1918:
        months[1]=15
        for index,month in enumerate(months):
            if days<=month :
                return '{:02}.{:02}.{:02} '.format(days,index+1,year)
            else:
                days-=month
    elif 1919 <= year <=2700:
        #Gregorian
        if year%400==0 or (year%4==0 and year%100!=0):
            months[1]=29
        for index,month in enumerate(months):
            if days<=month :
                return '{:02}.{:02}.{:04} '.format(days,index+1,year)
            else:
                days-=month
    else:
        return "Year out of bounds"

year = int(input().strip())
result = solve(year)
print(result)
