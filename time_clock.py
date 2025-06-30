"""
try-except blocks are used to capture valid user entries for the current time and the alarm hours
if-then decision control statements are used to make sure there are entries within the specified range
"""

ERR_MSG_1 = 'Please enter a valid time between 0 and 23 ❌'
ERR_MSG_2 = 'Please enter a valid non-negative integer ❌'

class TimeClock:
    def __init__(self):
        self.__time_clock_arr = []
        self.__current_time = None
        self.__alarm_hours = None
        self.__alarm_output_time = None
        self.__user_entries()
        self.__time_clock_init()
        self.__alarm_output()

    def __user_entries(self):
        while True:
            try:
                self.__current_time = int(input('Please enter the current time in hours between 0 and 23: '))
                if 0 <= self.__current_time <= 23:
                    break
                else:
                    print(ERR_MSG_1)
            except ValueError:
                print(ERR_MSG_1)
        while True:
            try:
                self.__alarm_hours = int(input('Please enter the alarm hours: '))
                if self.__alarm_hours < 0:
                    print(ERR_MSG_2)
                else:
                    break
            except (ValueError, OverflowError):
                print(ERR_MSG_2)


    def __time_clock_init(self):
        for num in range(0, 24):
            if num == 0:
                self.__time_clock_arr.append((num, '12 AM'))
            elif num > 12:
                self.__time_clock_arr.append((num, f'{num - 12} PM'))
            else:
                self.__time_clock_arr.append((num, f'{num} AM'))

    def __alarm_output(self):
        if self.__alarm_hours > 0:
            self.__time_clock_arr = self.__time_clock_arr * self.__alarm_hours
        self.__alarm_output_time = self.__time_clock_arr[self.__current_time + self.__alarm_hours]

    def get_alarm_output(self):
        return self.__current_time, self.__alarm_hours, self.__alarm_output_time