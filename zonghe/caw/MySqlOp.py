# @Time : 2021/2/23 15:55
# @Author:曹晶晶
# 　＠File : MySqlOp.py
'''操作数据的方法'''
import json

import pymysql

# 数据库连接
from zonghe.caw import DataRead


def connect(db_info):
    host = db_info['host']
    port = db_info['port']
    user = db_info['user']
    pwd = db_info['pwd']
    database = db_info['name']
    try:
        conn = pymysql.connect(host=host, user=user, password=pwd,
                               database=database, port=port, charset='utf8')
        print("连接成功")
    except Exception as e:
        print(f"连接失败，异常信息为:{e}")
    return conn


# 断开连接
def disconnect(conn):
    '''
        :param conn:
        :return:
    '''
    try:
        conn.close()
    except Exception as e:
        print(f"断开数据库连接失败，异常信息为:{e}")


# 执行数据库
def execute(conn, sql):
    try:
        cursor = conn.cursor()  # 获取游标
        cursor.execute(sql)  # 执行SQL语句
        conn.commit()  # 提交
        print("删除成功")
        cursor.close()  # 关闭游标
    except Exception as e:
        print(f"执行SQL语句失败，异常信息为：{e}")

def delete_user(mobilephone,db_info):
    '''
    :param mobilephone:
    :param db_info:
    :return:
    '''
    conn = connect(db_info)
    execute(conn, f"delete from member where mobilephone={mobilephone};")
    disconnect(conn)


if __name__ == '__main__':
    db_info = DataRead.read_ini(r"test_env\env.ini", "db_info")
    db_info = json.loads(db_info)
    delete_user("13073514019",db_info)

