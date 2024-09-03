"""
    pymysql创建数据库连接 改进版
"""
from pymysql import Connection

con = None

try:
    # 创建数据库连接
    con = Connection(
        host="localhost",  # 主机名
        port=3306,  # 端口
        user="root2",  # 账户
        password="123456"  # 密码
    )
    print(type(con))
    print(con.get_host_info())
    print(con.get_server_info())
except Exception as e:
    print("异常：", e)
finally:
    if con:
        # 关闭连接
        con.close()
