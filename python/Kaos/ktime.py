#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created: Aug 2017

    @author: 73RM1N41@9R0GR4M13
"""
import kerri
import time
from datetime import datetime

###################
# TIME MANAGEMENT #
###################

class Time(object):
    """ This class controls the flow of time in your program """

    def __init__(self):
        self.days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',
                4:'Friday', 5:'Saturday', 6:'Sunday'}

        self.months = {1:'January', 2:'February', 3:'March', 4:'April',5:'May',
                  6:'June', 7:'July', 8:'August', 9:'September', 10:'October',
                  11:'November', 12:'December'}

    def __str__(self):
        now = time.localtime(time.time())
        date = str("%s/%s/%s" % (now[1], now[2], now[0]))
        if now[3] == 0:
            hour = "0%s" % now[3]
            ampm = "am"
        else:
            pass
        if now[3] > 12:
            hour = now[3] - 12
            ampm = "pm"
        elif now[3] != 0 and now[3] <= 12 and now[3] >= 10:
            hour = "%s" % now[3]
            ampm = "am"
        else:
            hour = "0%s" % now[3]
            ampm = "am"
        if now[5] <= 9:
            second = "0%s" % now[5]
        else:
            second = now[5]
        if now[4] <= 9:
            min = "0%s" % now[4]
        else:
            min = now[4]
        ktime = str("%s:%s:%s %s" % (hour,min,second, ampm))
        return str(date)+"   "+str(ktime)

    def marker(self, *args):
        """
        Get Marker For Timing Things
        """

        if len(args) >= 1:
            raise kerri.ExcessArguments("marker()", 0)
        else:
            pass
        marker = time.time()
        return marker

    def wait(self, itime='1', *args):
        """ Wait for specified time {in seconds} before continuing """

        if len(args) >= 1:
            raise kerri.ExcessArguments("wait()", 1)
        else:
            pass
        time.sleep(itime)

    def now(self, *args):
        """ Return current date and time """

        if len(args) >= 1:
            raise kerri.ExcessArguments("now()", 0)
        else:
            pass
        return datetime.now()

    def p_now(self, *args):
        """ Return current date and time in user friendly format """

        if len(args) >= 1:
            raise kerri.ExcessArguments("p_now()", 0)
        else:
            pass
        now = time.localtime(time.time())
        day = now[6]
        return str("%s %s/%s/%s %s:%s:%s" % (self.days[day], now[1], now[2], now[0],
                                               now[3], now[4], now[5]))

    def c_hour(self, *args):
        """ Return the currnet hour """

        if len(args) >= 1:
            raise kerri.ExcessArguments("c_hour()", 0)
        else:
            pass
        now = time.localtime(time.time())
        hour = now[3]
        return hour

    def c_min(self, *args):
        """ Return the current minute [0-59]"""

        if len(args) >= 1:
            raise kerri.ExcessArguments("c_min()", 0)
        else:
            pass
        now = time.localtime(time.time())
        minute = now[4]
        return minute

    def c_sec(self, *args):
        """ Return the current second [0-59] """

        if len(args) >= 1:
            raise kerri.ExcessArguments("c_sec()", 0)
        else:
            pass
        now = time.localtime(time.time())
        second = now[5]
        return second

    def month(self, *args):
        """ Return current month [Returns months name not integer] """

        if len(args) >= 1:
            raise kerri.ExcessArguments("month()", 0)
        else:
            pass
        now = time.localtime(time.time())
        month = now[1]
        return self.months[month]

    def m_day(self, *args):
        """ Return the day of the month """

        if len(args) >= 1:
            raise kerri.ExcessArguments("m_day()", 0)
        else:
            pass
        now = time.localtime(time.time())
        d_month = now[2]
        return d_month

    def year(self, *args):
        """ Return the year """

        if len(args) >= 1:
            raise kerri.ExcessArguments("year()", 0)
        else:
            pass
        now = time.localtime(time.time())
        year = now[0]
        return year

    def _time(self, *args):
        """ Return the current time [HH:MM:SS]"""

        if len(args) >= 1:
            raise kerri.ExcessArguments("_time()", 0)
        else:
            pass
        now = time.localtime(time.time())
        if now[3] == 0:
            hour = "0%s" % now[3]
            ampm = "am"
        else:
            pass
        if now[3] > 12:
            hour = now[3] - 12
            ampm = "pm"
        elif now[3] != 0 and now[3] <= 12 and now[3] >= 10:
            hour = "%s" % now[3]
            ampm = "am"
        else:
            hour = "0%s" % now[3]
            ampm = "am"
        if now[5] <= 9:
            second = "0%s" % now[5]
        else:
            second = now[5]
        if now[4] <= 9:
            min = "0%s" % now[4]
        else:
            min = now[4]
        return str("%s:%s:%s %s" % (hour,min,second, ampm))

    def _date(self, *args):
        """ Return the current date [MM/DD/YY] """

        if len(args) >= 1:
            raise kerri.ExcessArguments("_date()", 0)
        else:
            pass
        now = time.localtime(time.time())
        return str("%s/%s/%s" % (now[1], now[2], now[0]))

    def w_day(self, *args):
        """ Return the current day of the week [Returns name of the
            day not integer value] {EX: Monday, Tuesday Wed...etc,.}"""

        if len(args) >= 1:
            raise kerri.ExcessArguments("w_day()", 0)
        else:
            pass
        now = time.localtime(time.time())
        day = now[6]
        return self.days[day]

    def y_day(self, *args):
        """ Return integer value of the current day of the year """

        if len(args) >= 1:
            raise kerri.ExcessArguments("y_day()", 0)
        else:
            pass
        now = time.localtime(time.time())
        d_num = now[7]
        return d_num

    def summer_chk(self, *args):
        """ Returns (1) if it is summer time, (0) if it is not and (-1)
            if it can not be determined """

        if len(args) >= 1:
            raise kerri.ExcessArguments("summer_chk()", 0)
        else:
            pass
        now = time.localtime(time.time())
        check = now[8]
        if check == 1:
            return 1, ":) It\'s Summer Time!!!"
        elif check == 0:
            return 0, ":( It\'s Not Summer Time!!!"
        else:
            return -1, "I\'m not even really sure who I am...\nI don\'t think I am qualified to answer that."

#########
# INITs #
#########

ktime = Time()
marker = ktime.marker
wait = ktime.wait
now = ktime.now
p_now = ktime.p_now
c_hour = ktime.c_hour
c_min = ktime.c_min
c_sec = ktime.c_sec
month = ktime.month
m_day = ktime.m_day
year = ktime.year
_time = ktime._time
_date = ktime._date
w_day = ktime.w_day
y_day = ktime.y_day
summer_chk = ktime.summer_chk
