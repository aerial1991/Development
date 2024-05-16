#pip install pymysql
from pymysql import Connection
con =Connection('localhost','root','123456','test_1')
print(type(con))








con.close()