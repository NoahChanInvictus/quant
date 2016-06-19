# -*- coding:utf-8 -*-
import sys
sys.path.append('../')
import json
from time_utils import today, yesterday
from global_utils import default_db
from global_config import SIGNAL_TABLE, STOCK_TABLE

def get_buy_signal_info():
    yesterday_date = yesterday()
    print yesterday_date
    conn = default_db()
    cur = conn.cursor()
    order = 'select id, stock_id, ref_invest, high_buy from ' + SIGNAL_TABLE + \
            ' where stock_status=0 and signal_date="%s"' % yesterday_date
    cur.execute(order)
    data = cur.fetchall()
    print len(data)
    cur.close()
    conn.close()

def get_sell_signal_info():
    conn = default_db()
    cur = conn.cursor()
    order = 'select id, stock_id, buy_share, low_sell, ref_sell_date from ' + SIGNAL_TABLE + \
            ' where stock_status=1'
    cur.execute(order)
    data = cur.fetchall()
    print len(data)
    cur.close()
    conn.close()

def trade_buy(signal_id, stock_id, price, share):
    today_date = today()
    direction = 'buy'
    conn = default_db()
    order = 'select account from ' + ACCOUNT_TABLE + ' order by id desc'
    cur.execute(order)
    account = cur.fetchone()[0]
    value = price * share
    order = 'select * from ' + SIGNAL_TABLE + 'where id=%d' % signal_id
    cur.execute(order)
    if cur.fetchone() != None:
        order = 'update ' + SIGNAL_TABLE + ' set stock_status=1, buy_share=%d, buy_price=%f, buy_date="%s" where id=%d' % (share, price, today_date, signal_id)
        cur.execute(order)
        order = 'insert into ' + STOCK_TABLE + ' (stock_id, direction, share, value, date) values ("%s", "%s", %d, %f, "%s")' % (stock_id, direction, share, value, today_date)
        cur.execute(order)
        order = 'insert into ' + ACCOUNT_TABLE + ' (account, date) values (%f, "%s")' % (account - value, today_date)
        cur.execute(order)
        conn.commit()
    cur.close()
    conn.close()

def trade_sell(signal_id, stock_id, price, share, net_value):
    today_date = today()
    direction = 'sell'
    conn = default_db()
    order = 'select account from ' + ACCOUNT_TABLE + ' order by id desc'
    cur.execute(order)
    account = cur.fetchone()[0]
    value = price * share
    order = 'select * from ' + SIGNAL_TABLE + 'where id=%d' % signal_id
    cur.execute(order)
    if cur.fetchone() != None:
        order = 'update ' + SIGNAL_TABLE + ' set stock_status=2, sell_share=%d, sell_price=%f, sell_date="%s" where id=%d' % (share, price, today_date, signal_id)
        cur.execute(order)
        order = 'insert into ' + STOCK_TABLE + ' (stock_id, direction, share, value, date) values ("%s", "%s", %d, %f, "%s")' % (stock_id, direction, share, value, today_date)
        cur.execute(order)
        order = 'insert into ' + ACCOUNT_TABLE + ' (account, date) values (%f, "%s")' % (account + net_value, today_date)
        cur.execute(order)
        conn.commit()
    cur.close()
    conn.close()

def trade_search(query_body, fields):
    conn = default_db()
    cur = conn.cursor()
    order = 'select %s' % ','.join(fields) + ' from ' + STOCK_TABLE
    if 'stock_id' in query_body:
        order += ' where stock_id="%s"' % query_body['stock_id']
    cur.execute(order)
    data = cur.fetchall()
    print len(data)
    cur.close()
    conn.close()

if __name__ == '__main__':
    #query_body = {'stock_id':'00025.SZ'}
    #fields = ['stock_id, direction, share, value, date']
    #trade_search(query_body, fields)
    #get_buy_signal_info()
    get_sell_signal_info()
