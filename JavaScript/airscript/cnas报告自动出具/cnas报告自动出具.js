//此脚本是用于检测中心cnas报告自动出具。适用于金山文档：CNAS检测报告。https://www.kdocs.cn/l/ciXZkBO5L1c9

const sht = Application.Sheets("cnas报告初版")
const ysbh = sht.Range("B:B").Find("原始编号").Offset(0,2).Value

//新建表已原始编号命名
const newsht = Application.Sheets.Add(
  null,
  Application.ActiveSheet.Name,
  1,
  Application.Enum.XlSheetType.xlWorksheet,
  ysbh
)

sht.Range("A1:L"+sht.UsedRange.RowEnd).EntireRow.Copy(newsht.Range("A1"))
newsht.Range("A1:L"+sht.UsedRange.RowEnd).Select()
Selection.PasteSpecial(xlPasteColumnWidths, xlPasteSpecialOperationNone, false, false);
Selection.PasteSpecial(xlPasteValuesAndNumberFormats, xlPasteSpecialOperationNone, false, false);

let startrow =newsht.Range("B:B").Find("序号").Row+2
const data = newsht.Range(`B${startrow}:L${sht.UsedRange.RowEnd}`).Value
let deleteList = []
let res = {},key
let 保留的设备={},key2

for (let i = 0; i < data.length; i++) {
  if (!(data[i][0] + "").includes(".")) { 
    key = i + startrow
    key2 = data[i][0]
    ke2val =data[i][1]
    deleteList.push(i+startrow)
   } else {
    if (data[i][7] == "" || data[i][7] == null) { deleteList.push(i+startrow)} else {
      if (res[key]) { res[key].push(data[i][7]) } else { res[key] = [data[i][7]] 
      }
      保留的设备[key2] = ke2val
    }
  }
}

//删除检测行
for(let i = deleteList.length-3;i>=0;i--){
 if(!res[[deleteList[i]]]){newsht.Rows(deleteList[i]).Delete()}

}

//算序号
let xuhao = []
let yiji = 1
for(let key in res){
  xuhao.push([yiji])
  for(let i=0;i<res[key].length;i++){
    xuhao.push([`${yiji}.${i+1}`])
  }
  yiji++
}

newsht.Range("B"+startrow).Resize(xuhao.length,1).Value =xuhao
//删除设备行
let 设备起始行 = newsht.Range("B:B").Find("主要仪器设备及编号").Row

for(let i =10;i>0;i--){
  if(!保留的设备[i]){newsht.Rows(i+设备起始行-1).Delete()}
  
}

let jcxmlist = Object.values(保留的设备)

newsht.Range("D"+(设备起始行-2)).Value = jcxmlist[0]
newsht.Range("H"+(设备起始行-2)).Value = jcxmlist.length