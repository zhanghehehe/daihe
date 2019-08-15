# -*- coding: UTF-8 -*-
import pymysql
import xlrd
def sql_connect():
        bangbang = pymysql.connect(user="root", password="Pt^*w1Fd9", port=3306, db="jyfq-order", host="123.57.22.1",
                                   charset="utf8")
        cur = bangbang.cursor()
        cur.execute("select pid,user_name from t_order where id = '547640510091035392'")
        sql = cur.fetchall()
        return (sql)
        cursor.close()
        bangbang.commit()
        bangbang.close()
re = sql_connect()
for i in re:
    l = i[0]
    print(l)
for s in re:
    y = s[0]
    print (y)
#print (re)