from datetime import datetime, timedelta


def digit_count(input_string):  # 13.09
    uppers = 0
    input_list = input_string.split()
    for i in input_list:
        uppers_local = 0
        for j in i:
            if j.isupper():
                uppers_local += 1
        if uppers_local > len(i) - uppers_local:
            uppers += 1
    print(f"{int(uppers / len(input_list) * 100)}%")


def date_check(day, month, year):
    leap = False
    day_max = 30
    if year > 0:
        if year % 100 == 0:
            leap = False
        if year % 4 == 0 or year & 400 == 0:
            leap = True
        if 12 > month > 1:
            if month % 2 == 0:
                day_max = 31
                if month == 2 and leap:
                    day_max = 29
                elif month == 2 and not leap:
                    day_max = 28
            if day <= day_max:
                return True
    return False


# print(date_check(29,21,2020))

def diary(records, start_date):
    file = open("diary", "w")
    for i in range(len(records)):
        file.write(str((datetime.strptime(start_date, '%d-%m-%Y')
                        + timedelta(days=i)).strftime('%d-%m-%Y'))
                   + " " + str(records[i]) + '\n')


diary(["мы тонем", "я нашел ящик рома", "все не так плохо"], "15-07-2004")
