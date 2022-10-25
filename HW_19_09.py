def date_check(day, month, year):
    """Function validate date and return True or False as a result"""
    leap = False
    day_max = 30
    if year > 0:
        if year % 100 == 0:
            leap = False
        if year % 4 == 0 or year & 400 == 0:
            leap = True
        if 1 < month <= 12:
            if month % 2 == 0:
                day_max = 31
                if month == 2 and leap:
                    day_max = 29
                elif month == 2 and not leap:
                    day_max = 28
            if day <= day_max:
                return True
    return False
