#!/usr/bin/env python3
'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py 
Author: "Aileen Orilloza"
The python code in this file (a1_amcorilloza.py) is original work written by "Aileen Orilloza". No code in this file is copied from any other source except those provided by the course instructor, including any person, textbook, or on-line resource. I have not shared this python script with anyone or anything except for submission for grading. I understand that the Academic Honesty Policy will be enforced and violators will be reported and appropriate action will be taken.

'''


import sys


def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7

    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else:
        return days_in_month.get(month, 31)


def after(date: str) -> str:
    '''after() -> date for next day in YYYY-MM-DD string format
    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582

    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day + 1

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)
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


def usage():
    "Print a usage message to the user"
    print("Usage: python3 assignment1.py start_date end_date")
    print("Example: python3 assignment1.py 2023-05-01 2023-05-30")


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    try:
        year, month, day = map(int, date.split('-'))

        if month < 1 or month > 12:
            return False

        if day < 1 or day > mon_max(month, year):
            return False

        return True
    except ValueError:
        return False


def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    start_year, start_month, start_day = map(int, start_date.split('-'))
    stop_year, stop_month, stop_day = map(int, stop_date.split('-'))

    weekend_count = 0
    current_date = f"{start_year}-{start_month:02}-{start_day:02}"

    while True:
        weekday = day_of_week(current_year, current_month, current_day)

        if weekday == 'sat' or weekday == 'sun':
            weekend_count += 1

        next_date = after(current_date)
        current_year, current_month, current_day = map(int, next_date.split('-'))

        if current_year == stop_year and current_month == stop_month and current_day == stop_day:
            break

    return weekend_count


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)
    start_date = sys.argv[1]
    stop_date = sys.argv[2]
    weekend_days = day_count(start_date, stop_date)
    print(f"The number of weekend days between {start_date} and {stop_date} is {weekend_days}.")
