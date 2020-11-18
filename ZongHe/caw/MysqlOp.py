"""
数据库操作
1、数据库从mysql换成sqlite，脚本层不用改动，只需要改动caw里的mysql.py以及本文件
2、这部分访问到业务的数据库了，所以放baw中
"""

# 连接数据库
import pymysql


def connect(db):
    """
    连接数据库
    :param db:一个字典，存储数据库信息
    :return:
    """
    # db={"ip":"jy001","port":4406,"dbName":"future","username":"root","pwd":"123456"}
    host = db["ip"]
    port = int(db["port"])
    user = db["username"]
    name = db["dbName"]
    pwd = db["pwd"]
    try:
        conn = pymysql.connect(host=host, port=port, user=user, password=pwd, database=name, charset='utf8')
        print(f"数据库{host}:{port}连接成功")
        return conn
    except Exception as e:
        print(f"数据库连接异常，异常信息为：{e}")


# 断开数据库连接
def disconnect(conn):
    try:
        conn.close()
        print("断开数据库连接成功")
    except Exception as e:
        print(f"断开数据库连接失败，异常信息为:{e}")


# 执行sql语句
def execute(conn, sql):  # 连接相当于建了一条到数据库的路
    try:
        cursor = conn.cursor()  # 获取游标，相当于在路上跑的一辆车，通过车把数据取回来
        cursor.execute(sql)  # 执行sql语句
        conn.commit()  # 提交
        cursor.close()  # 关闭游标
        print(f"执行sql语句{sql}成功")
    except Exception as e:
        print(f"执行sql语句{sql}失败，异常信息为：{e}")


if __name__ == '__main__':
    db = {"ip": "jy001", "port": 4406, "dbName": "future", "username": "root", "pwd": "123456"}
    conn = connect(db)
    execute(conn,'delete from Member where MobilePhone = 13938383841;')
    disconnect(conn)
