# -*- coding:utf-8 -*-

import sys
sys.path.append('../')
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
    order = 'select id, middle_on, strict_flag, static_closing, date from ' + SETTINGS_TABLE 
    cur.execute(order)
    data = cur.fetchall()
    print data
    cur.close()
    conn.close()

def settings_modify(modify_dict):
    today_date = today()
    conn = default_db()
    cur = conn.cursor()
    order = 'select middle_on, strict_flag, static_closing from ' + SETTINGS_TABLE + ' order by id desc' 
    cur.execute(order)
    middle_on, strict_flag, static_closing = cur.fetchone()

    if 'middle_on' in modify_dict:
        middle_on = modify_dict['middle_on']
    if 'strict_flag' in modify_dict:
        strict_flag = modify_dict['strict_flag']
    if 'static_closing' in modify_dict:
        static_closing = modify_dict['static_closing']

    order = 'insert into ' + SETTINGS_TABLE + '(middle_on, strict_flag, static_closing, date) ' \
            + 'values(%d, %d, %d, "%s")' % (middle_on, strict_flag, static_closing, today_date)
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
    #modify_dict = {'strict_flag': 1}
    #settings_modify(modify_dict)
    settings_search()
