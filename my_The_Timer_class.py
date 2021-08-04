# Your class will be called Timer. Its constructor accepts three arguments representing hours
# (a value from range [0..23] - we will be using the military time),
# minutes (from range [0..59])
# and seconds (from range [0..59]).

# Zero is the default value for all of the above parameters.
# There is no need to perform any validation checks.

# The class itself should provide the following facilities:

# objects of the class should be "printable",
# i.e. they should be able to implicitly convert themselves into strings
# of the following form: "hh:mm:ss",
# with leading zeros added when any of the values is less than 10;

# the class should be equipped with parameterless methods
# called next_second() and previous_second(),
# incrementing the time stored inside objects by +1/-1 second respectively.

# all object's properties should be private;
# consider writing a separate function (not method!) to format the time string.

class Timer:
    def __init__(self, hrs=0, min=0, secs=0):
        self.hrs = hrs
        self.min = min
        self.secs = secs

    def __str__(self):
        time = time_format(self.hrs) + ":" + \
            time_format(self.min) + ":" + time_format(self.secs)
        return time

    def next_second(self):
        self.secs += 1
        if self.secs == 60:
            self.secs = 0
            self.min += 1
        if self.min == 60:
            self.min = 0
            self.hrs += 1
        if self.hrs == 24:
            self.secs = self.min = self.hrs = 0

    def prev_second(self):
        self.secs -= 1
        if self.secs == -1:
            self.secs = 59
            self.min -= 1
        if self.min == -1:
            self.min = 59
            self.hrs -= 1
        if self.hrs == -1:
            self.secs = self.min = 59
            self.hrs = 23


def time_format(num):
    if num < 10:
        num = "0" + str(num)
    else:
        num = str(num)
    return num


print("start")
timer = Timer(23, 59, 59)
print(timer)  # 23:59:59

print("+1")
timer.next_second()
print(timer)  # 00:00:00
print("-1")
timer.prev_second()
print(timer)  # 23:59:59
print()
print("start")
timer = Timer(0, 0, 59)
print(timer)  # 23:59:59
print("+1")
timer.next_second()
print(timer)  # 00:00:00
print()
print("start")
timer = Timer(8, 0, 0)
print(timer)  # 23:59:59
print("-1")
timer.prev_second()
print(timer)  # 23:59:59
