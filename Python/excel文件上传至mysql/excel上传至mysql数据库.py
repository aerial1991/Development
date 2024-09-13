import pandas as pd
import pymysql
import os


# 读取Excel文件
excel_file = 'D:/0829B.xlsx'
sheet_name = 'Sheet1'
# 使用os.path.splitext分离文件名和扩展名
file_name_without_extension, file_extension = os.path.splitext(excel_file)
file_name = os.path.basename(file_name_without_extension)
print(file_name)  # 输出: file
tablename =file_name+'_'+sheet_name
df = pd.read_excel(excel_file,sheet_name=sheet_name)
print(sheet_name)
print()
df_filled = df.fillna('')

# 连接MySQL数据库
connection = pymysql.connect(host='10.91.0.66', user='root', password='Admin*123', db='test')

try:
    # 使用cursor()方法获取操作游标
    with connection.cursor() as cursor:
        # 创建SQL语句，根据表头生成CREATE TABLE语句
        columns = ', '.join([f'`{col}` VARCHAR(255)' for col in df_filled.columns])
        print(df_filled.columns.name)
        print(columns)
        cursor.execute(f'drop table IF EXISTS {tablename}')
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {tablename} ({columns})"

        # 执行SQL语句
        cursor.execute(create_table_sql)
        for index, row in df_filled.iterrows():
            insert_query = f"INSERT INTO {tablename} VALUES {tuple(row.values)}"
            print(row.values)
            cursor.execute(insert_query)

        # 提交到数据库执行
        connection.commit()
        print(f"Table {tablename} created successfully.")
finally:
    connection.close()