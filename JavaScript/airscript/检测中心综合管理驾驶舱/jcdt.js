
//此脚本是用于检测部大屏动态数据自动提取。适用于金山文档：检测-大屏展示数据源

let range = Application.Sheets("动态数据-检测").UsedRange
let [nul,head, ...data] = range.Value
let today = getNowDate()
let todaylist = []
// console.log(data)
for (let item of data) {
  m= item[2]<10 ?'0'+item[2]:item[2]
  d= item[3]<10 ?'0'+item[3]:item[3]
  const weituoriqi = `${item[1]}/${m}/${d}`
  if (weituoriqi == today) {
    todaylist.push(item)
  } 
//   // console.log(todaylist)
}

console.log(todaylist)

function getNowDate() {
  const date = new Date()
  const year = date.getFullYear()
  const month = (date.getMonth() + 1).toString().padStart(2, "0")
  const day = date.getDate().toString().padStart(2, "0")
  return `${year}/${month}/${day}`
}
	
// 3hs7ch709411.vicp.fun:45192
const connection = SQL.connect(SQL.Drivers.MySQL, {
  host: '3hs7ch709411.vicp.fun',
  username: 'root',
  password: 'Admin*123',
  database: 'zhijian',
  port: 45192
})


for (let i=0;i<todaylist.length;i++){
  id= todaylist[i][0]
  console.log(id)
const result1 = connection.queryAll(
  `DELETE FROM test_day WHERE ID = ${id}`)
const result2 = connection.queryAll(
  'INSERT INTO test_day (Year, Month, Day, Number_Daily_Commissions, Completed_Quantity, In_Progress_Quantity, ID) VALUES (?,?,?,?,?,?,?)',
  [todaylist[i][1],todaylist[i][2],todaylist[i][3],todaylist[i][4],todaylist[i][5],todaylist[i][6],todaylist[i][0]]
)
}


// // 执行SQL语句，插入数据
// const result2 = connection.queryAll(
//   'INSERT INTO test (id,test_data) VALUES (?,?), (?,?)',
//   [1, 1, 2, 2]
// )
// // 打印执行结果
// console.log(result2)

// 关闭数据库连接
connection.close()






// const result1 = connection.queryAll(
//   'DELETE FROM test_day WHERE ID = (?)',res
// )