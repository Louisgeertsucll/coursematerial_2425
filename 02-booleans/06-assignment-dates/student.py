# write your code hereµ
def is_valid_month(month):
    return 1<=month<=12
          
def is_leap_year(year):
    if (year%4==0):
        if (year%100==0):
            if (year%400==0):
                return True
            else:
                return False
        else:
            return True
    else: 
        return False

def has_30_days(month):
    return month == 4 or month == 6 or month == 9 or month == 11
    
def has_31_days(month):
    return month == 1 or month ==3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 
    
def has_28_days(month, year):
    if month == 2 and not is_leap_year(year):
        return True
    else :
        return False
    
def has_29_days(month, year):
    if month == 2 and is_leap_year(year):
         return True
    else:
        return False
    
def is_valid_date(day, month, year):
    if not is_valid_month(month):
        return False
    elif month == 2:
        if has_28_days(month, year):
            return 1 <= day <= 28
        elif has_29_days(month, year):
            return 1 <= day <= 29
        else:
            return False
    elif has_30_days(month):
        return 1 <= day <= 30
    elif has_31_days(month):
        return 1 <= day <= 31
    else:
        return False




