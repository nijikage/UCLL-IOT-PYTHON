months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_days_of_month(number):
    if number > len(months) or number <= 0:
        return 0
    else:
        return months[(number-1)]


def days_from_start_year(number):
    if number > len(months) or number <= 0:
        return 0
    else:
        total = 0
        for month in months[0:number]:
            total = total + month
        return total


def days_until_end_year(number):
    if number > len(months) or number <= 0:
        return 0
    else:
        total = 0
        for month in months[number:len(months)]:
            total = total + month
        return total


def days_between_months(starting_month, ending_month):
    if starting_month > len(months) or starting_month < 0:
        return 0
    elif starting_month > ending_month:
        return 0
    elif starting_month == 0:
        return days_from_start_year(ending_month)
    else:
        total = 0
        for month in months[starting_month:ending_month]:
            total = total + month
        return total


print(get_days_of_month(1))  # prints 31
print(get_days_of_month(2))  # prints 28 
print(get_days_of_month(12))  # prints 31

print(get_days_of_month(-5))  # prints 0 because 0 <= 0
print(get_days_of_month(0))   # prints 0 because 0 <= 0
print(get_days_of_month(13))  # prints 0 because 13 > 12

print(days_from_start_year(1))   # prints 31
print(days_from_start_year(2))   # prints 59
print(days_from_start_year(3))   # prints 90
print(days_from_start_year(12))  # prints 365 

print(days_until_end_year(1))   # prints 334
print(days_until_end_year(2))   # prints 306
print(days_until_end_year(12))  # prints 0

print(days_between_months(1, 2))   # prints 28
print(days_between_months(1, 3))   # prints 59
