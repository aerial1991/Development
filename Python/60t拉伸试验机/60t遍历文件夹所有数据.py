import re
import pymysql
import os

def list_files(directory):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            if filename.endswith('_0.html') and filename[-8:-7].isdigit():
              print(path)  # 是文件则打印文件路径
              # file_path = 'D:/HuaweiMoveData/Users/47469/Desktop/CLS0506_0.html'
              # 打开文件并读取内容
              with open(path, 'r') as file:
                  html_content = file.read()
              list1 = []
              obj = re.compile(r'<span class = ".*?" style = ".*?">(?P<result>.*?)</span>')
              result = obj.finditer(html_content)
              for item in result:
                  re1 = item.group("result")
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
        elif os.path.isdir(path):
            list_files(path)  # 是文件夹则递归调用


# 使用示例：
directory_path = 'D:/HuaweiMoveData/Users/47469/Desktop/60t数据'  # 替换为你的目录路径
list_files(directory_path)










#
# # 设置文件夹路径
# folder_path = 'D:/HuaweiMoveData/Users/47469/Desktop/60t数据'
#
# # 遍历文件夹
# for filename in os.listdir(folder_path):
#     # print(filename)
#     if filename.endswith(r'_0.html'):
#         # 读取文件内容
#         file_path = os.path.join(folder_path, filename)
#         with open(file_path, 'r') as file:
#             content = file.read()
#             # print(content)
# #
# #
# # # 假设文件位于D盘根目录下
# #D:\HuaweiMoveData\Users\47469\Desktop\CLS0506.files\CLS0506.files
# file_path = 'D:/HuaweiMoveData/Users/47469/Desktop/CLS0506_0.html'
# # 打开文件并读取内容
# with open(file_path, 'r') as file:
#     html_content = file.read()
# list1 = []
# obj = re.compile(r'<span class = ".*?" style = ".*?">(?P<result>.*?)</span>')
# result = obj.finditer(html_content)
# for item in result:
#     re1= item.group("result")
#     list1.append(re1)
# print(list1)
# print(len(list1))
#
# # MySQL数据库连接信息
# mysql_host = '10.91.0.66'
# mysql_user = 'root'
# mysql_password = 'Admin*123'
# mysql_db = 'zhijian'
# mysql_table1 = '60t'
# # 建立MySQL数据库连接
# connection = pymysql.connect(
#     host=mysql_host,
#     user=mysql_user,
#     password=mysql_password,
#     database=mysql_db
# )
# cursor = connection.cursor()
# insert_query = f"INSERT INTO {mysql_table1} VALUES {tuple(list1)}"
# cursor.execute(insert_query)
# connection.commit()
# cursor.close()
# connection.close()