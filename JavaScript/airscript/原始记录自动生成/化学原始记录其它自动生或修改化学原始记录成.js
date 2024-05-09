//此脚本是用于检测中心修改化学元素或其它设备的原始记录。适用于金山文档：02-HX分析原始记录。https://www.kdocs.cn/l/cnBoFtsGxNMM

let range = Application.Sheets("其它").UsedRange
const sht = Application.Sheets("化学原始")

let [nul,nul1,head, ...data] = range.Value
let bh = []
for(let item of data){
const hh= sht.Range("F:F").Find(`${item[5]}`).Row
bh.push(item[5])
console.log(hh)
for(let ele=0;ele<item.length; ele++){
  console.log(ele)
    if(ele != null){
  sht.Cells(hh,ele+1).Value =item[ele]
  } 

}
}