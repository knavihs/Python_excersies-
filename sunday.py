import calendar

year = 2018
x = []
day_to_count = calendar.SUNDAY
for month in range(1,13):
    matrix = calendar.monthcalendar(year,month)
    num_days = sum(1 for x in matrix if x[day_to_count] != 0)
    y = calendar.month_abbr[month]
    print(y)
    print(num_days)
    if num_days >= 5:
        x.append(y)


print(x)
#print(num_days)
#print(calendar.month_abbr[3])