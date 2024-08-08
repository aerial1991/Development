import pandas as pd
# df = pd.read_excel('data.xlsx', sheet_name='Sheet1', header=0)
# 读取Excel文件中的Sheet1
df = pd.read_excel('D:/0120.xlsx', sheet_name='Sheet1')

# 筛选出G列不包含"-"的行
filtered_df = df[df['G'].str.contains('-', regex=False) == False]

# 从筛选出的结果中读取I列的值
filtered_values = filtered_df['I'].values

print(filtered_values)


