"""
    pymysql创建数据库连接 最基础写法
"""
from pymysql import Connection

# 创建数据库连接
con = Connection(
    host="localhost",  # 主机名
    port=3306,  # 端口
    user="root",  # 账户
    password="123456"  # 密码
)
print(type(con))
print(con.get_host_info())
print(con.get_server_info())

# 关闭连接
con.close()
