# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


class Days(object):

    Day = 1
    Weekday = 1
    Month = 1
    Year = 1900
    Sundays = 0
    LeapYear = (1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948,
                1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000)

    def __init__(self, Day=1, Month=1, Weekday=1, Year=1900, Sundays=0,
                 LeapYear=(1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932,
                           1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964,
                           1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996,
                           2000)):

        self.Day = Day
        self.Month = Month
        self.Year = Year
        self.Sundays = Sundays
        self.LeapYear = LeapYear
        self.Weekday = Weekday

    def Advance_Day(self):

        if self.Month in [4, 6, 8, 11]:
            if self.Day <= 29:
                self.Day += 1
                if self.Weekday == 7:
                    self.Weekday = 1
                if self.Weekday < 7:
                    self.Weekday += 1
            if self.Day == 30:
                self.Day = 1
                self.Month += 1
                if self.Weekday == 7:
                    self.Weekday = 1
                if self.Weekday < 7:
                    self.Weekday += 1

        if self.Month in [1, 3, 5, 7, 9, 10, 12]:
            if self.Day <= 30:
                self.Day += 1
                if self.Weekday == 7:
                    self.Weekday = 1
                if self.Weekday < 7:
                    self.Weekday += 1
            if self.Day == 31:
                self.Day = 1
                if self.Weekday == 7:
                    self.Weekday = 1
                if self.Weekday < 7:
                    self.Weekday += 1
                if self.Month <= 11:
                    self.Month += 1
                if self.Month == 12:
                    self.Month = 1
                    self.Year += 1

        if self.Month == 2:
            if self.Year in self.LeapYear:
                if self.Day <= 28:
                    self.Day += 1
                    if self.Weekday == 7:
                        self.Weekday = 1
                    if self.Weekday < 7:
                        self.Weekday += 1
                if self.Day == 29:
                    self.Day = 1
                    self.Month += 1
                    if self.Weekday == 7:
                        self.Weekday = 1
                    if self.Weekday < 7:
                        self.Weekday += 1

            if self.Year not in self.LeapYear:
                if self.Day <= 27:
                    self.Day += 1
                    if self.Weekday == 7:
                        self.Weekday = 1
                    if self.Weekday < 7:
                        self.Weekday += 1
                if self.Day == 28:
                    self.Day = 1
                    self.Month += 1
                    if self.Weekday == 7:
                        self.Weekday = 1
                    if self.Weekday < 7:
                        self.Weekday += 1

        if self.Weekday == 7 and self.Day == 0:
            self.Sundays += 1

counter = Days()
while counter.Year < 2001:
    counter.Advance_Day()
    print counter.Weekday
print counter.Sundays


