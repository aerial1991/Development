import pandas as pd
import pymysql

# 连接MySQL数据库
connection1 = pymysql.connect(host='10.97.0.17', user='custom_readonly', password='qQRek8q9tuykzCRz', db='imp_plm')


cursor = connection1.cursor()

sql1 ="""SELECT
	pa.CODE AS 物料编码,
	pa.NAME AS 名称,
	pa.model AS 型号,
	pa.figure_no AS 图号,
	pa.specification AS 规格,
	pa.material AS 材料,
	def.define1 AS 执行标准,
	pa.part_type AS 零部件类型,
	ba.NAME AS 业务属性,
	cgr.CODE AS 物料类型编码,
	tkfile.name_attribute AS 名称属性,
	pa.creationtime AS 创建时间,
	ur.name as 创建人
FROM
	imp_plm_p_m_part pa
	LEFT JOIN imp_plm_p_m_def def ON pa.id = def.id
	LEFT JOIN imp_plm_p_m_cgr cgr ON pa.partclassid = cgr.id
	LEFT JOIN imp_plm_p_busattr_base ba ON pa.selfmade = ba.id
	LEFT JOIN tkkgl_db.imp_plm_p_b_l_file tkfile ON pa.name_attribute = tkfile.id
	LEFT JOIN iuap_uuas_usercenter.USER ur ON pa.creator = ur.yht_user_id 	
WHERE
	pa.dr = 0 
	AND pa.ytenant_id = 'jpgfp4ia' 
	AND pa.lifecyclestate != '1613019747583525147'
	and ur.yht_tenant_id = 'jpgfp4ia'"""

cursor.execute(sql1)

results = cursor.fetchall()
for row in results:
    print(row[0])


# # 连接MySQL数据库
connection2 = pymysql.connect(host='10.91.0.66', user='root', password='Admin*123', db='test')

cursor2 = connection2.cursor()
#在数据库中创建表
sql2="""CREATE TABLE IF NOT EXISTS yfwl (
	物料编码 VARCHAR (255),
	名称 VARCHAR (255),
	型号 VARCHAR (255),
	图号 VARCHAR (255),
	规格 VARCHAR (255),
	材料 VARCHAR (255),
	执行标准 VARCHAR (255),
	零部件类型 VARCHAR (255),
	业务属性 VARCHAR (255),
	物料类型编码 VARCHAR (255),
	名称属性 VARCHAR (255),
	创建时间 VARCHAR (255),
	创建人 VARCHAR (255)
	)"""
cursor2.execute(sql2)
connection2.commit()

# 清空表
sql3 ="TRUNCATE TABLE yfwl"
cursor2.execute(sql3)
connection2.commit()

for row in results:
    物料编码 =row[0]
    名称=row[1]
    型号=row[2]
    图号=row[3]
    规格=row[4]
    材料=row[5]
    执行标准=row[6]
    零部件类型=row[7]
    业务属性=row[8]
    物料类型编码=row[9]
    名称属性=row[10]
    创建时间=row[11]
    创建人=row[12]
    sql3=""" insert into yfwl(物料编码,名称,型号,图号,规格,材料,执行标准,零部件类型,业务属性,物料类型编码,名称属性,创建时间,创建人) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor2.execute(sql3,(物料编码,名称,型号,图号,规格,材料,执行标准,零部件类型,业务属性,物料类型编码,名称属性,创建时间,创建人))
    connection2.commit()

    # 关闭数据库
connection1.close()
connection2.close()

