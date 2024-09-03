import pandas as pd
import re
from tkinter import filedialog
# 选择一个文件
file_path = filedialog.askopenfilename(title='请选择一个Excel表', filetypes=[('Excel','.xls .xlsx'),('文本','.txt'),('All Files', '*')],initialdir='E:\\',multiple=True)

# 读取规则表并将采购件规则分配到字典中
def load_rules(rules_df):
    like_dict = {}
    for _, row in rules_df.iterrows():
        component = row['名称']
        result_value = str(row['物料分类'])
        match_type = row['匹配类型']
        if match_type == 'like':
            add_to_dict(like_dict, component, result_value)
            print(f"处理行 {like_dict}:")
    return like_dict

# 向字典中添加规则
def add_to_dict(target_dict, component, result_value):
    target_dict[component] = result_value

# 获取匹配值的函数
def get_matching_value(component, match_dict,match_type):
    if match_type == 'like':
        # 对于like匹配，遍历字典键，检查component是否包含在键中
        for key in match_dict:
            if key in component:
                return match_dict[key]
    else:
        if component in match_dict:
            return match_dict[component]

    # 如果未匹配到，返回空字符串
    return ""


# 主逻辑：读取Sheet并进行替换
def update_ming_chen_shu_xing_test(file_path):
    # 读取数据
    df = pd.read_excel(file_path, sheet_name='Sheet1',dtype=str)
    rules_df = pd.read_excel(file_path, sheet_name='采购件', dtype=str)

    # 确保列名没有前后空格
    df.columns = df.columns.str.strip()
    rules_df.columns = rules_df.columns.str.strip()

    # 加载规则到字典
    like_dict = load_rules(rules_df)

    # 确保数据列为字符串
    df['流程'] = df['流程'].astype(str)
    df['新名称'] = df['新名称'].astype(str)
    df['图号'] = df['图号'].astype(str)
    df['材料名称'] = df['材料名称'].astype(str)

    # 初始化新列
    df['物料分类'] = ""

    # 遍历数据并进行匹配
    for i, row in df.iterrows():
        currentSeq = row['零件部件']
        currentSeq1 = row['制造方式']
        currentSeq3 = row['序号']
        currentSeq4 = row['流程']
        currentSeq5 = row['图号']
        currentSeq6 = row['材料名称']

        print(f"处理行 {i}:")
        print(f"  零件部件: {currentSeq}")
        print(f"  制造方式: {currentSeq1}")
        print(f"  序号: {currentSeq3}")
        print(f"  流程: {currentSeq4}")
        print(f"  图号: {currentSeq5}")
        print(f"  材料名称: {currentSeq6}")

        if currentSeq4[:1] in ["D", "d"]:
            matched_value = get_matching_value( currentSeq2, like_dict,match_type='like')
            print(f"  匹配值: {matched_value}")
            if matched_value:
                df.at[i, '物料分类'] = matched_value
            else:
                df.at[i, '物料分类'] = ""
    # 保存结果到新文件
    output_file = 'E:/output.xlsx'
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)

    # 获取工作簿和工作表对象
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 设置"物料分类"列为文本格式
    format = workbook.add_format({'num_format': '@'})
    col_idx = df.columns.get_loc('物料分类')  # 获取"物料分类"列的位置
    worksheet.set_column(col_idx, col_idx, None, format)  # 设置列格式
    print(f"结果已保存到 {output_file}")

# 调用主逻辑
update_ming_chen_shu_xing_test(file_path[0])