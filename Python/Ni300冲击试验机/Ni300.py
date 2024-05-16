import sqlite3
import pymysql
import pandas as pd

# 连接到SQLite数据库
conn = sqlite3.connect('D:/Impact.db')

# 使用SQL查询语句获取数据并将其存储在DataFrame中
query = "SELECT * FROM sample;"
df = pd.read_sql_query(query, conn)
df.replace([None], 'N/A', inplace=True)
# 打印DataFrame
# 关闭数据库连接
print(df)
conn.close()

# MySQL数据库连接信息
mysql_host = '10.91.0.66'
mysql_user = 'root'
mysql_password = 'Admin*123'
mysql_db = 'zhijian'
mysql_table1 = 'impact'
# 建立MySQL数据库连接
connection = pymysql.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_db
)
cursor = connection.cursor()
# 执行SQL语句
cursor.execute('SELECT * FROM impact')
results = cursor.fetchall()
# 定义一个判断列表
list1 = []
for r in results:
    list1.append(r[1])
print(list1)
for index, row in df.iterrows():
    # print(index,row.values)
    if list1.count(row[1]) == 0 :
        insert_query = f"INSERT INTO {mysql_table1} VALUES {tuple(row.values)}"
        cursor.execute(insert_query)

connection.commit()
cursor.close()
connection.close()
