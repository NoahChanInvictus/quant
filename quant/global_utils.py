# -*- coding:utf-8 -*-
import pymysql
from global_config import SQL_HOST, SQL_USER, SQL_PASSWD, SQL_DB, SQL_CHARSET

def default_db(host=SQL_HOST, user=SQL_USER, passwd=SQL_PASSWD, db=SQL_DB, charset=SQL_CHARSET):
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, charset=charset)
    return conn
