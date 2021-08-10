# 4.6.1.13 LAB: the calendar module

# extend its functionality with a new method called count_weekday_in_year,
# which takes a year and a weekday as parameters,
# and then returns the number of occurrences of a specific weekday in the year.

# Create a class called MyCalendar that extends the Calendar class;
# create the count_weekday_in_year method with the year and weekday parameters.
# The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday.
# The method should return the number of days as an integer;
# in your implementation, use the monthdays2calendar method of the Calendar class.

import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, week_day):
        week_count = 0
        for month in range(12):
            for days in self.monthdays2calendar(year, month + 1):
                for day in days:
                    if day[0] != 0 and day[1] == week_day:
                        #print(month+1, day[0])
                        week_count += 1
        return week_count


my_cal = MyCalendar()

num_days_a = my_cal.count_weekday_in_year(2019, calendar.MONDAY)  # 52
# num_days_b = my_cal.count_weekday_in_year(2019, 0) #52
print(num_days_a)

num_days_a = my_cal.count_weekday_in_year(2000, calendar.SUNDAY)  # 53
# num_days_b = my_cal.count_weekday_in_year(2000, 6) #53

#num_days_a = my_cal.count_weekday_in_year(2021, calendar.WEDNESDAY)
# num_days_b = my_cal.count_weekday_in_year(2021, 2)

print(num_days_a)
