//此脚本是用于校准部大屏动态数据自动提取。适用于金山文档：校准-大屏展示数据源


let range = Application.Sheets("客户委托情况").UsedRange
let [nul,head, ...data] = range.Value
let res=[]

for (let item of data) {
  const numDate = item[2];
  const date = new Date((numDate - 25569) * 86400 * 1000);
  const year = date.getFullYear()
  const month = (date.getMonth() + 1).toString().padStart(2, "0")
  const day = date.getDate().toString().padStart(2, "0")
  const weituoriqi = `${year}/${month}/${day}`;
  if (item[2] != '') {
    item[2] = weituoriqi
    res.push(item)
  }
}
console.log(res)
// for (let i=0;i<data.length;i++){
//   if(data[i][2]==''){
//     break
//   }
// res.push(data[i])
// }
// console.log(res)
// let today = getNowDate()
// let todaylist = []
// // let b =Application.Sheets("客户委托情况").Range('c3').Value
// // let a = new Date((b- 25569)*86400*1000)
// // const  c = a.getFullYear()

// // console.log(c)
// // console.log(data)
// for (let item of data) {
//   const numDate = item[2]
//   const date = new Date((numDate - 25569) * 86400 * 1000)
//   const year = date.getFullYear()
//   const month = (date.getMonth() + 1).toString().padStart(2, "0")
//   const day = date.getDate().toString().padStart(2, "0")
//   const weituoriqi = `${year}/${month}/${day}`
//   if (weituoriqi == today) {
//     todaylist.push(item)
//   } 
// //   // console.log(todaylist)
// }

// console.log(todaylist)

// function getNowDate() {
//   const date = new Date()
//   const year = date.getFullYear()
//   const month = (date.getMonth() + 1).toString().padStart(2, "0")
//   const day = date.getDate().toString().padStart(2, "0")
//   return `${year}/${month}/${day}`
// }
	
// 3hs7ch709411.vicp.fun:45192
const connection = SQL.connect(SQL.Drivers.MySQL, {
  host: '3hs7ch709411.vicp.fun',
  username: 'root',
  password: 'Admin*123',
  database: 'zhijian',
  port: 45192
})


// 执行SQL语句，插入数据
const result2 = connection.queryAll(
  'TRUNCATE TABLE calibration_customer_commission'
)
// 打印执行结果
console.log(result2)

for (let i=0;i<res.length;i++){
const result3 = connection.queryAll(
  'INSERT INTO calibration_customer_commission (ID, Entrusting_Date, Customer_Name, Model, Original_Name, Samples_Number) VALUES (?,?,?,?,?,?)',
  [res[i][0],res[i][2],res[i][3],res[i][4],res[i][5],res[i][6]]
)
console.log(result3)
}

// // // 关闭数据库连接
connection.close()