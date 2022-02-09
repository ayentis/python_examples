


# class MyCalendar(calendar.Calendar):
#
#     def count_weekday_in_year(self, year, weekday):
#
#         rez = self.yeardatescalendar(year)
#         for r in rez:
#             print(r)
#
# x = MyCalendar()
# x.count_weekday_in_year(2020, 6)

import calendar

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)