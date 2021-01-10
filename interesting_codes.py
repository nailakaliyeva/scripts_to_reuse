def is_a_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

print(is_a_leap_year(1900))


def num_of_days_in_a_month(month, year):
    days_nums = [False, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 and month > 12:
        return "Please, enter a number between 1 and 12"
    elif month == 2 and is_a_leap_year(year):
        return 29
    else:
        return days_nums[month]