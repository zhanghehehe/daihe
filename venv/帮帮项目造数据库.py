# -*- coding: UTF-8 -*-
import pandas
import pymysql
import xlrd
bangbang = pymysql.connect(user="root",password="Pt^*w1Fd9",port=3306,db="jyfq-order",host="123.57.22.1",charset="utf8")
cursor = bangbang.cursor()
sql = "select * from t_order where pid = 1471520"
#sql_1 = "insert into t_order(pid) values(100001)"
#df = pandas.read_excel(r"C:\Users\windows\Desktop\work.xlsx")
df = xlrd.open_workbook(r"C:\Users\windows\Desktop\work.xlsx")
df_1 = df["create_date"],["version"]
#i = 0
#for i in df_1:
#   print ("请输入日期：",i)
#   print (name)
rs = cursor.execute(sql)
#bangbang.close()
print (rs)
print (df_1)