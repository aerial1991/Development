import openpyxl

# 打开Excel文件
workbook = openpyxl.load_workbook('D:/111.xlsx')

# 选择sheet页1
sheet = workbook['Sheet1']

# 获取A列的值并处理
for cell in sheet['B']:
    if cell.value is not None:
        value = str(cell.value)
        if '-' in value:
            # 删除最后一个-及后面的内容
            value = value[:value.rindex('-')]
        # 将处理后的值放入B列
        sheet.cell(row=cell.row, column=4).value = value

# 保存修改后的Excel文件
workbook.save('D:/111.xlsx')