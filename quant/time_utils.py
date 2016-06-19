# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta
import time

def today():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))

def yesterday():
    return datetime2datestr(datetime.now() - timedelta(days = 1))

def now():
    return time.strftime('%H:%M:%S', time.localtime(time.time()))

def datetime2datestr(date):
    return date.strftime('%Y-%m-%d')

def unix2hadoop_date(ts):
    return time.strftime('%Y_%m_%d', time.localtime(ts))

def ts2datetime(ts):
    return time.strftime('%Y-%m-%d', time.localtime(ts))

def ts2date(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

def ts2date_min(ts):
    return time.strftime('%Y-%m-%d %H:%M', time.localtime(ts))

def datetime2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d')))

def window2time(window, size=24*60*60):
    return window*size

def datetimestr2ts(date):
    return time.mktime(time.strptime(date, '%Y%m%d'))

def ts2datetimestr(ts):
    return time.strftime('%Y%m%d', time.localtime(ts))

def ts2HourlyTime(ts, interval):
    # interval 取 Minite、Hour
    ts = ts - ts % interval
    return ts

def ts2datetime_full(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ts))

if __name__=='__main__':
    date = today()
    #date = ts2datetime(1456934400)
    print 'date:', date
