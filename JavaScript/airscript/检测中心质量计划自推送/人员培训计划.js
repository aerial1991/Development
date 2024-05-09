//此脚本是用于检测中心质量计划自动推送。适用于金山文档：人员培训计划。https://www.kdocs.cn/l/cuQm4eDvcGA5

let range = Application.Sheets("Sheet1").UsedRange
let [head, ...data] = range.Value
let today = getNowDate()
let todaylist = []
for (let item of data) {
  const numDate = item[2];
  const date = new Date((numDate - 25569) * 86400 * 1000);
  const year = date.getFullYear()
  const month = (date.getMonth() + 1).toString().padStart(2, "0")
  const day = date.getDate().toString().padStart(2, "0")
  const jihuadate = `${year}/${month}/${day}`;
  if (jihuadate == today) {
    item[2] = jihuadate
    todaylist.push(item)
  } else if (jihuadate < today&& jihuadate >"19000101" &&item[11] !== "是") {
    item[2] = jihuadate
    todaylist.push(item)
  }
}
// console.log(todaylist)
for (let item of todaylist) {
  let email = [item[8], item[9],item[10]]
  email.push("474694014@qq.com")
  console.log(email)
  let res = []
  for (let i = 1; i < 8; i++) {
    res.push(`【${head[i]}】：${item[i]}`)
  }
  let subject = item[1]
  let html = `<p>${res.join("<br>")}<br> <a href="https://www.kdocs.cn/l/cuQm4eDvcGA5">https://www.kdocs.cn/l/cuQm4eDvcGA5</a></p>`
  sendemail(subject, html, email)
  Time.sleep(1000)
  console.log(res)
}

function getNowDate() {
  const date = new Date()
  const year = date.getFullYear()
  const month = (date.getMonth() + 1).toString().padStart(2, "0")
  const day = date.getDate().toString().padStart(2, "0")
  return `${year}/${month}/${day}`
}

function sendemail(subject, html, email) {
  let mailer = SMTP.login({
    host: "smtp.qq.com", // 域名
    port: 465, // 端口
    secure: true, // TLS
    username: "474694014@qq.com", // 账户名
    password: "zyiytcicxpfubjdc" // 密码
  })
  mailer.send({
    from: "人员培训提醒<474694014@qq.com>",
    to: email,
    subject: subject,
    html: html
  })
}

