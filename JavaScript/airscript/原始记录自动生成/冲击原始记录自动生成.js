//此脚本是用于检测中心原始记录自动生成。适用于金山文档：04-CJ冲击检测原始记录。https://www.kdocs.cn/l/cuUkWLOthUhh

const connection = SQL.connect(SQL.Drivers.MySQL, {
    host: '3hs7ch709411.vicp.fun',
    username: 'root',
    password: 'Admin*123',
    database: 'zhijian',
    port: 45192
  })
  // 执行SQL语句，查询test表的所有数据
  const result1 = connection.queryAll('SELECT * FROM impact LIMIT 1489, 18446744073709551615')
  
  let dataObject = result1.rows
  let dataArray=dataObject.map(row =>row.map(item =>item.value))
  Application.Sheets('impact').Range('C2:AA'+(dataArray.length+1)).Value=dataArray
  console.log(dataArray)
  // 关闭数据库连接
  connection.close()
  
  
  