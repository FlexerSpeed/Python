def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def DaysInMonth(year, month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= month <= 12:
        if month == 2 and is_leap_year(year):
            return 29
        else:
            return days_in_month[month]
    else:
        return None


def DayOfYear(year, month, day):
    if not (1 <= month <= 12) or not (1 <= day <= DaysInMonth(year, month)):
        return None

    cumulative_days = sum(DaysInMonth(year, m) for m in range(1, month))
    cumulative_days += day

    return cumulative_days


print(DayOfYear(2000, 12, 31))
