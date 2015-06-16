#!/usr/bin/env python
# encoding: utf-8
"""
play_at_random_time.py

Created by Rachel on 2014-02-07.
"""

from datetime import datetime
from random import randint
import time
import webbrowser

def wait_until_time(start_time):
    # turn start_time into a datetime object
    start_hour, start_min = map(int, start_time.split(":"))
    now = datetime.now()
    start = datetime(now.year, now.month, now.day, start_hour, start_min)

    # calculate difference between start time and the current time
    wait_time = start - now

    # sleep until start time
    time.sleep(wait_time.seconds)

def open_webpage(url):
    webbrowser.open_new_tab(url) 


if __name__ == '__main__':
    h = randint(14,17)
    m = randint(0,59)
    # h = 19
    # m = 49
    start_time = "%s:%s"%(h,m)
    url = 'http://www.youtube.com/watch?v=3RRrNWF46Ns&t=1m3s'
    wait_until_time(start_time)
    
    open_webpage(url)
    
