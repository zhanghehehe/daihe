import flask
import pymysql
import json
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
from flask import request
server = flask.Flask(__name__)
@server.route('/login/query', methods=['get'])
def login():
    username = request.values.get('name')
    pwd = request.values.get('pwd')
    if username and pwd:
        sql_res = sql_connect()
        for p in sql_res:
            #print (p)
            q = p[0]
            u = p[1]
            #print (u)
            if username == 'u' and pwd == 'q':
                print (q)
                #print (q)
                resu = {'code': 200, 'message': '登录成功'}
                return json.dumps(resu, ensure_ascii=False)  # 将字典转换字符串
            elif username == 'zhang' and pwd == '666':
                resu = {'code':404,'message':'未找到页面'}
                return json.dumps(resu, ensure_ascii=False)
            else:
                resu = {'code': -1, 'message': '账号密码错误'}
                return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 10001, 'message': '参数不能为空！'}
        return json.dumps(resu, ensure_ascii=False)
if __name__ == '__main__':
    server.run(debug=True, port=8888, host='127.0.1.1')