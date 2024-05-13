import tkinter as tk
from tkinter import messagebox

def main():
    # 在这里编写你的程序
    # D:Results.csv

    import dbfread
    import pandas as pd
    import pymysql
    # import re
    # import os
    # 指定DBF文件的路径
    dbf_file_path = 'E:/30t/Lzc.dbf'
    # MySQL数据库连接信息
    mysql_host = '10.91.0.66'
    mysql_user = 'root'
    mysql_password = 'Admin*123'
    mysql_db = 'zhijian'
    mysql_table1 = '30t'
    # 建立MySQL数据库连接
    connection = pymysql.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db
    )
    # 创建游标
    cursor = connection.cursor()

    table = dbfread.DBF(dbf_file_path, encoding='GBK')
    records = [record for record in table]
    df = pd.DataFrame(records)
    # 执行SQL语句
    cursor.execute('SELECT * FROM 30t')
    results = cursor.fetchall()
    print(results)
    print(df)
    list1 = []
    for r in results:
        list1.append(r[0])
    for index, row in df.iterrows():

        if list1.count(row[0]) == 0:
            print(row[0])
            # insert_query = f"INSERT INTO {mysql_table1} VALUES {tuple(row.values)}"
            insert_query = f"INSERT INTO {mysql_table1} VALUES {tuple(row.values)} "
            # print(row.values)
            cursor.execute(insert_query)

    connection.commit()
    cursor.close()
    connection.close()
    pass

if __name__ == "__main__":
    main()
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("提示", "上传成功！")
