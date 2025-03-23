#!/usr/bin/env python3
#AuthorID: amcorilloza

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    lyear = year % 4
    if lyear == 0:
        feb_max = 29 # this is a leap year
    else:
        feb_max = 28 # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        feb_max = 28 # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        feb_max = 29 # this is a leap year

    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    tmp_day = day + 1  # next day

    if tmp_day > mon_max[month]:
        to_day = tmp_day % mon_max[month]  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date

