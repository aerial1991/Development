
import pandas as pd
import pymysql
import re
import os

# CSV文件路径
csv_file_path = 'D:/Thermo/Oxsas_Data/Export/Results.csv'

# MySQL数据库连接信息
mysql_host = '10.91.0.66'
mysql_user = 'root'
mysql_password = '***'
mysql_db = '***'
mysql_table1 = 'felast'
mysql_table2 = 'fecrni'
mysql_table3 = 'fecrst'

largest_column_count = 0
with open(csv_file_path, 'r') as temp_f:
    lines = temp_f.readlines()
    for l in lines:
        column_count = len(l.split(',')) + 1
        # 找到列数最多的行
        largest_column_count = column_count if largest_column_count < column_count else largest_column_count
temp_f.close()
# colunm_names为最大列数展开
column_names = [i for i in range(0, largest_column_count)]

df = pd.read_csv(csv_file_path, header=None, delimiter=',', names=column_names)
df_filled = df.fillna('null')
# 建立MySQL数据库连接
connection = pymysql.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_db
)
# 创建游标
cursor = connection.cursor()
print(df_filled)
print("---------------------------")

felast_df = df_filled[df_filled[6] == 'FELAST  '].iloc[:,0:83]
fecrni_df = df_filled[df_filled[6] == 'FECRNI  '].iloc[:,0:86]
fecrst_df = df_filled[df_filled[6] == 'FECRst  '].iloc[:,0:80]
print(df_filled[14])
print(felast_df)
print("******************")
print(fecrni_df)
# 插入数据
for index,row in felast_df.iterrows():
    insert_query = f"INSERT INTO {mysql_table1} VALUES {tuple(row.values)}"
    print(row.values)
    cursor.execute(insert_query)
for index,row in fecrni_df.iterrows():
    insert_query = f"INSERT INTO {mysql_table2} VALUES {tuple(row.values)}"
    print(row.values)
    cursor.execute(insert_query)
for index,row in fecrst_df.iterrows():
    insert_query = f"INSERT INTO {mysql_table3} VALUES {tuple(row.values)}"
    print(row.values)
    cursor.execute(insert_query)


os.remove(csv_file_path)
# 提交更改并关闭连接
connection.commit()
cursor.close()
connection.close()
