"""
    pymysql执行DDL语句
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
        database="db_python"  # 指定操作的数据库
    )
    # 创建游标对象
    cursor = con.cursor()

    # 定义一个建表sql语句
    sql = """
        CREATE TABLE `t_student2` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(10) DEFAULT NULL,
      `age` int(11) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    """

    # 选择要操作的数据库
    # con.select_db("db_python")

    # 使用游标对象，执行sql
    cursor.execute(sql)

    # cursor.close() 可以省略
except Exception as e:
    print("异常：", e)
finally:
    if con:
        # 关闭连接
        con.close()
