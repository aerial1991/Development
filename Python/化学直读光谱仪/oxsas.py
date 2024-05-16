#该版本适用于相同试验方法的文件上传，不同方法会报错。不同方法的数据上传参照下个版本。
import tkinter as tk
from tkinter import messagebox
#化学制度光谱仪脚本最终版，注意编译的时候必须在win7下编译，否则会报错
def main():
    # 在这里编写你的程序
    # D:Results.csv

    import pandas as pd
    import pymysql
    import re
    import os
    # CSV文件路径
    csv_file_path = 'D:/Results.csv'

    # MySQL数据库连接信息
    mysql_host = '10.91.****'
    mysql_user = '****'
    mysql_password = '****'
    mysql_db = '******'
    mysql_table1 = 'felast'
    mysql_table2 = 'fecrni'
    mysql_table3 = 'fecrst'

    # 读取CSV文件到DataFrame
    df = pd.read_csv(csv_file_path, header=None)
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

    print("---------------------------")

    # # 创建表格（如果不存在）
    # create_table_query = f'''
    #     CREATE TABLE IF NOT EXISTS {mysql_table} (
    #         {', '.join([f'{col} TEXT' for col in df.columns])}
    #     )
    # '''
    # cursor.execute(create_table_query)

    # 插入数据
    for index, row in df_filled.iterrows():
        print(index)
        print("---------------------------")
        bb = row[6]
        print('原始带空格的' + bb)
        dd = bb.replace(' ', '')
        print('替换后不带空格的' + dd)
        ee = re.sub('  ', '', bb)
        print(ee)
        is_equal1 = (dd == 'FECRNI')
        print(is_equal1)
        print(len(row))
        if dd == 'FELAST':
            insert_query = f"INSERT INTO {mysql_table1} VALUES {tuple(row.values)}"
            print(row.values)
            cursor.execute(insert_query)
        elif dd == 'FECRNI':
            insert_query = f"INSERT INTO {mysql_table2} VALUES {tuple(row.values)}"
            print(row.values)
            cursor.execute(insert_query)
        elif dd == 'FECRST':
            insert_query = f"INSERT INTO {mysql_table3} VALUES {tuple(row.values)}"
            cursor.execute(insert_query)

        # insert_query = f"INSERT INTO {mysql_table} VALUES {tuple(row.values)}"
    os.remove(csv_file_path)
    # 提交更改并关闭连接
    connection.commit()
    cursor.close()
    connection.close()

    pass

if __name__ == "__main__":
    main()
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("提示", "上传成功！")
