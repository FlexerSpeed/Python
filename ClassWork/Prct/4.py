# --- Task four ---
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def get_days_in_month(year, month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= month <= 12:
        if month == 2 and leap_year(year):
            return 29
        else:
            return days_in_month[month]
    else:
        return None


testyears = [1900, 2000, 2016, 1987]
testmonths = [2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
    yr = testyears[i]
    mo = testmonths[i]
    print(yr, mo, "->", end=" ")
result = get_days_in_month(yr, mo)
if result == testresults[i]:
    print("OK")
else:
    print("Failed")
