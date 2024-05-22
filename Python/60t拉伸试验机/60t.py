#该脚本用于将固定一个html文件内容插入到MySQL数据库中
import re
import pymysql
import pandas as pd
# 假设文件位于D盘根目录下
#D:\HuaweiMoveData\Users\47469\Desktop\CLS0506.files\CLS0506.files
file_path = 'D:/HuaweiMoveData/Users/47469/Desktop/CLS0506_0.html'
# 打开文件并读取内容
with open(file_path, 'r') as file:
    html_content = file.read()
list1 = []
obj = re.compile(r'<span class = ".*?" style = ".*?">(?P<result>.*?)</span>')
result = obj.finditer(html_content)
for item in result:
    re1= item.group("result")
    list1.append(re1)
print(list1)
print(len(list1))

# MySQL数据库连接信息
mysql_host = '10.91.0.66'
mysql_user = 'root'
mysql_password = 'Admin*123'
mysql_db = 'zhijian'
mysql_table1 = '60t'
# 建立MySQL数据库连接
connection = pymysql.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_db
)
cursor = connection.cursor()
insert_query = f"INSERT INTO {mysql_table1} VALUES {tuple(list1)}"
cursor.execute(insert_query)
connection.commit()
cursor.close()
connection.close()