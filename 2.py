#Number of days per month. First value placeolder for indexing purposes.
#Lista nr de sfirsit a 12 luni in an.
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]


def is_leap(year):
    # Return True for leap years, False for non-leap years.
    # An bisect 1/4 ani
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    #Daca year diviz cu 4 si nu este div cu 100 sau divizibil cu 400

def days_in_mnth(year, month):
    # Return number of days in that month in that year.
    #"Nr de zile in aceasta luna"
    if not 1 <= month <= 12:
        return "Invalid Month"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))
#An bisect 1/4 ani

print(days_in_mnth(2017, 2))
# "Nr de zile in aceasta luna"
