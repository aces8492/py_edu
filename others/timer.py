#!/usr/bin/python
# coding: UTF-8

# display now date and time
import datetime # import datetime module
import time
import re

#set timer
target = input("please input time hh:mm:ss : ")
if not re.match('[0-9]{2}:[0-9]{2}:[0-9]{2}', target):
    print("input error")
    exit()

target_h = int(target[0:2])
target_m = int(target[3:5])
target_s = int(target[6:8])

#timer guarantee for time gap
target_s_in = target_s + 1

print("date = {0}:{1}:{2}".format(target_h, target_m, target_s))

# get now date and time using today method
#  {module.class.method()}
end_count = 0
start_flag = 1

#start timer
while True:
    d = datetime.datetime.today()
    #adjust 1loop = 1sec reference other function delay
    time.sleep(0.9999999)
    print('d = {}'.format(d))
    end_count += 1
    if((d.hour == target_h and d.minute == target_m) and (d.second == target_s or d.second == target_s_in)):
        print("now is a time!")
        break
        
