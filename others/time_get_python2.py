#!/usr/bin/python
# coding: UTF-8

# display now date and time
import datetime # import datetime module

# get now date and time using today method
#  {module.class.method()}
d = datetime.datetime.today()

# display raw data
print 'd = %s' % d
# display year month day
print '%s年%s月%s日' % (d.year, d.month, d.day)
# display time (h, min, sec, usec)
print '%s時%s分%s.%s秒' % (d.hour, d.minute, d.second, d.microsecond)
