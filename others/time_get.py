#!/usr/bin/python
# coding: UTF-8

# display now date and time
import datetime # import datetime module

# get now date and time using today method
#  {module.class.method()}
d = datetime.datetime.today()

# display raw data
print('d = {}'.format(d))
# display year month day
print('{0}年{1}月{2}日'.format(d.year, d.month, d.day))
# display time (h, min, sec, usec)
print('{0}時{1}分{2}.{3}秒'.format(d.hour, d.minute, d.second, d.microsecond))
