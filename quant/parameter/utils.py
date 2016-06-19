# -*- coding:utf-8 -*-
import sys
sys.path.append('../')
import json
from time_utils import today
from global_utils import default_db
from global_config import PARAMETER_TABLE, SETTINGS_TABLE

def nct_update(true_list, false_list):
    today_date = today()
    conn = default_db()
    cur = conn.cursor()
    for i in true_list:
        order = 'update ' + PARAMETER_TABLE + ' set status=1, modify_date="%s" where id=%d' % (today_date, i)
        cur.execute(order)
    for j in false_list:
        order = 'update ' + PARAMETER_TABLE + ' set status=1, modify_date="%s" where id=%d' % (today_date, i)
        cur.execute(order)
    conn.commit()
    cur.close()
    conn.close()

def nct_create(market_type, status, window_length, conf_width, trade_gap):
    today_date = today()
    conn = default_db()
    cur = conn.cursor()
    order = 'select * from ' + PARAMETER_TABLE + ' where market_type="%s" and window_length=%d and conf_width=%f and trade_gap=%d' \
            % (market_type, window_length, conf_width, trade_gap)
    cur.execute(order)
    if cur.fetchone() == None:
        order = 'insert into ' + PARAMETER_TABLE + '(market_type, status, window_length, conf_width, trade_gap, modify_date) ' \
                + 'values("%s", %d, %d, %f, %d, "%s")' % (market_type, status, window_length, conf_width, trade_gap, today_date)
        cur.execute(order)
        conn.commit()
    else:
        print 'exist'
    cur.close()
    conn.close()

def nct_delete(del_list):
    conn = default_db()
    cur = conn.cursor()
    for i in del_list:
        order = 'delete from ' + PARAMETER_TABLE + ' where id=%d' % i
        cur.execute(order)
    conn.commit()
    cur.close()
    conn.close()

def nct_search(query_dict):
    conn = default_db()
    cur = conn.cursor()
    order = 'select * from ' + PARAMETER_TABLE
    if 'market_type' in query_dict:
        order += ' where market_type="%s"' % query_dict['market_type']
    cur.execute(order)
    data = cur.fetchall()
    print data
    cur.close()
    conn.close()

def settings_search():
    today_date = today()
    conn = default_db()
    cur = conn.cursor()
    order = 'select id, middle_on, strict_flag, static_closing, stocks, date from ' + SETTINGS_TABLE 
    cur.execute(order)
    data = cur.fetchall()
    print data
    cur.close()
    conn.close()

def settings_modify(modify_dict):
    today_date = today()
    conn = default_db()
    cur = conn.cursor()
    order = 'select middle_on, strict_flag, static_closing, stocks from ' + SETTINGS_TABLE + ' order by id desc' 
    cur.execute(order)
    middle_on, strict_flag, static_closing, stocks = cur.fetchone()

    if 'middle_on' in modify_dict:
        middle_on = modify_dict['middle_on']
    if 'strict_flag' in modify_dict:
        strict_flag = modify_dict['strict_flag']
    if 'static_closing' in modify_dict:
        static_closing = modify_dict['static_closing']
    if 'stocks' in modify_dict:
        stocks = modify_dict['stocks']

    order = 'insert into ' + SETTINGS_TABLE + '(middle_on, strict_flag, static_closing, stocks, date) ' \
            + 'values(%d, %d, %d, "%s", "%s")' % (middle_on, strict_flag, static_closing, stocks, today_date)
    cur.execute(order)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    #query_dict = {'market_type':'down'}
    #nct_search(query_dict)
    #nct_create('test', 0, 1, 1, 1)
    #nct_update([26], [])
    #nct_delete([26])
    #settings_search()
    modify_dict = {'strict_flag': 1}
    stock_nos = ['00011.SZ','00012.SZ','00016.SZ','00017.SZ','00018.SZ','00019.SZ','00020.SZ','00022.SZ','00025.SZ','00026.SZ',\
                 '00028.SZ','00029.SZ','00030.SZ','00037.SZ','00045.SZ','00055.SZ','00056.SZ','00058.SZ','00413.SZ','00418.SZ',\
                 '00429.SZ','00488.SZ','00505.SZ','00521.SZ','00530.SZ','00539.SZ','00541.SZ','00550.SZ','00553.SZ','00570.SZ',\
                 '00581.SZ','00596.SZ','00613.SZ','00625.SZ','00725.SZ','00726.SZ','00761.SZ','00869.SZ']
    modify_dict['stocks'] = ','.join(stock_nos)
    #settings_modify(modify_dict)
