-- plm系统数据库
-- host：10.97.0.17
-- user：custom_readonly 
-- port：3306
-- password：qQRek8q9tuykzCRz




-- plm系统研发物料数据导出，选择imp_plm库，然后查询一下代码
SELECT
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
	and ur.yht_tenant_id = 'jpgfp4ia'


