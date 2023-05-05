from datetime import date, timedelta, time

# 1 Complete read_date()
def read_date():
    """Read a string representing a date in the format 2121-04-12, create a
    date object from the input string, and return the date object
    """
    dateStr = input()
    d = date.fromisoformat(dateStr)
    return d
    #print(type(d),d.month,d.day,d.year)


# 2. Use read_date() to read four (unique) date objects, putting the date objects in a list
d1 = read_date()
print(d1)
d2 = read_date()
print(d2)
d3 = read_date()
print(d3)

# 3. Use sorted() to sort the dates, earliest first

# 4. Output the sorted_dates in order, earliest first, in the format mm/dd/yy

# 5. Output the number of days between the last two dates in the sorted list
#    as a positive number

# 6. Output the date that is 3 weeks from the most recent date in the list

# 7. Output the full name of the day of the week of the earliest day
