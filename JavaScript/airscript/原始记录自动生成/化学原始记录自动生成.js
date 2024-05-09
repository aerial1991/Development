
//此脚本是用于检测中心原始记录自动生成。适用于金山文档：02-HX分析原始记录。https://www.kdocs.cn/l/cnBoFtsGxNMM
const connection = SQL.connect(SQL.Drivers.MySQL, {
    host: '3hs7ch709411.vicp.fun',
    username: 'root',
    password: 'Admin*123',
    database: 'zhijian',
    port: 45192
  })
  // 执行SQL语句，查询felast表的所有数据
  const result11 = connection.queryAll(
    `DELETE FROM felast WHERE a14 = 3 OR a13 = 0`)
  const result1 = connection.queryAll('SELECT * FROM felast')
  
  let dataObject = result1.rows
  let dataArray=dataObject.map(row =>row.map(item =>item.value))
  Application.Sheets('felast').Range('C2:CG'+(dataArray.length+1)).Value=dataArray
  console.log(dataArray)
  
  // 执行SQL语句，查询fecrni表的所有数据
  const result22 = connection.queryAll(
    `DELETE FROM fecrni WHERE a14 = 3  OR a13 = 0`)
  const result2= connection.queryAll('SELECT * FROM fecrni')
  
  let dataObject2 = result2.rows
  let dataArray2=dataObject2.map(row =>row.map(item =>item.value))
  Application.Sheets('fecrni').Range('C2:CJ'+(dataArray2.length+1)).Value=dataArray2
  console.log(dataArray2)
  
  // 执行SQL语句，查询fecrst表的所有数据
  const result33 = connection.queryAll(
    `DELETE FROM fecrst WHERE a14 = 3 OR a13 = 0`)
  const result3 = connection.queryAll('SELECT * FROM fecrst')
  
  let dataObject3 = result3.rows
  let dataArray3=dataObject3.map(row =>row.map(item =>item.value))
  Application.Sheets('fecrst').Range('C2:CD'+(dataArray3.length+1)).Value=dataArray3
  console.log(dataArray3)
  
  // 关闭数据库连接
  connection.close()
  
  