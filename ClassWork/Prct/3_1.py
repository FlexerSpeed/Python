def IsYearLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


testdata = [1900, 2000, 2016, 1987]
testresults = [False, True, True, False]

for i in range(len(testdata)):
    yr = testdata[i]
    print(yr, "->", end=" ")
    result = IsYearLeap(yr)

if result == testresults[i]:
    print("OK")
else:
    print("Failed")


def DaysInMonth(year, month):
    day_in_mouth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (0 >= month < 12) or (year <= 0):
        return None

    if month == 2 and IsYearLeap(year):
        return 29
    else:
        return day_in_mouth[month]


testyears = [1900, 2000, 2016, 1987]
testmonths = [2, 2, 1, 11]
testresults = [28, 29, 31, 30]

for i in range(len(testyears)):
    yr = testyears[i]
    mo = testmonths[i]
    print(yr, mo, "->", end=" ")
    result = DaysInMonth(yr, mo)

if result == testresults[i]:
    print("OK")
else:
    print("Failed")


def DayOfYear(year, month, day):

    if not (1 <= month <= 12) or not (0 < day <= DaysInMonth(year, month)):
        return None

    number_of_day = sum(DaysInMonth(year, m) for m in range(1, month))
    number_of_day += day
    return number_of_day


print(DayOfYear(2000, 12, 31))
