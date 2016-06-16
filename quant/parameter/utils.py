# -*- coding:utf-8 -*-

from time_utils import today
from global_utils import default_db
from global_config import PARAMETER_TABLE

def nct_update(true_list, false_list):
    today = today()
    conn = default_db()
    cur = conn.cursor()
    for i in true_list:
        order = 'update ' + PARAMETER_TABLE + ' set status=1, modify_date="%s" where id=%d' % (today, i)
        cur.execute(order)
    for j in false_list:
        order = 'update ' + PARAMETER_TABLE + ' set status=1, modify_date="%s" where id=%d' % (today, i)
        cur.execute(order)
    cur.commit()
    cur.close()
    conn.close()

def nct_create(market_type, status, window_length, conf_width, trade_gap):
    today = today()
    conn = default_db()
    cur = conn.cursor()
    order = 'insert into ' + PARAMETER_TABLE + '(market_type, status, window_length, conf_width, trade_gap, modify_date) ' \
            + 'values("%s", %d, %d, %f, %d, "%s")' % (market_type, status, window_length, conf_width, trade_gap, today)
    cur.execute(order)
    cur.commit()
    cur.close()
    conn.close()

def nct_delete(del_list):
    conn = default_db()
    cur = conn.cursor()
    for i in del_list:
        order = 'delete ' + PARAMETER_TABLE + 'where id=' + i
        cur.execute(order)
    cur.commit()
    cur.close()
    conn.close()
