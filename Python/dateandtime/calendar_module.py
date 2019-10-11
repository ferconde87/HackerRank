from datetime import date
l = list(map(int, input().split()))
d = date(month=l[0], day=l[1], year=l[2])
daysOfTheWeek = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(daysOfTheWeek[d.weekday()])

