"""
    pymysql执行update更新操作
"""
from pymysql import Connection

con = None

try:
    # 创建数据库连接
    con = Connection(
        host="localhost",  # 主机名
        port=3306,  # 端口
        user="root",  # 账户
        password="123456",  # 密码
        database="db_python",  # 指定操作的数据库
        autocommit=True  # 设置自动提交
    )
    # 创建游标对象
    cursor = con.cursor()

    # 使用游标对象，执行sql
    cursor.execute("update t_student2 set age=19 where id=5")

except Exception as e:
    print("异常：", e)
finally:
    if con:
        # 关闭连接
        con.close()
