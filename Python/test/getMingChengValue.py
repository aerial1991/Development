import pandas as pd

# 读取规则表并将规则分配到不同的字典中
def load_rules(rules_df):
    equal_dict = {}
    like_dict = {}

    for _, row in rules_df.iterrows():
        system_part = row['系统']
        component = row['部件']
        condition = row['条件字段']
        result_value = row['结果字段']
        match_type = row['匹配类型']

        if match_type == '=':
            add_to_dict(equal_dict, system_part, component, condition, result_value)
        elif match_type == 'like':
            add_to_dict(like_dict, system_part, component, condition, result_value)

    return equal_dict, like_dict

# 向字典中添加规则
def add_to_dict(target_dict, system_part, component, condition, result_value):
    if system_part not in target_dict:
        target_dict[system_part] = {}
    if component not in target_dict[system_part]:
        target_dict[system_part][component] = {}
    target_dict[system_part][component][condition] = result_value

# 获取匹配值的函数
def get_matching_value(system_part, component, condition, equal_dict, like_dict):
    # 先进行等于匹配
    if system_part in equal_dict:
        if component in equal_dict[system_part]:
            if condition in equal_dict[system_part][component]:
                return equal_dict[system_part][component][condition]

    # 再进行like匹配
    if system_part in like_dict:
        if component in like_dict[system_part]:
            for key in like_dict[system_part][component].keys():
                if condition in key:
                    return like_dict[system_part][component][key]

    # 如果未匹配到，返回空字符串
    return ""

# 主逻辑：读取Sheet并进行替换
def update_ming_chen_shu_xing_test(file_path):
    # 读取数据
    df = pd.read_excel(file_path, sheet_name='Sheet7')
    rules_df = pd.read_excel(file_path, sheet_name='Rules')

    # 加载规则到字典
    equal_dict, like_dict = load_rules(rules_df)

    # 初始化新列
    df['新列'] = ""

    # 遍历数据并进行匹配
    for i, row in df.iterrows():
        currentSeq = row['零部件类别']
        currentSeq1 = row['制造方式']
        currentSeq2 = row['新名称']
        currentSeq3 = row['序号']
        currentSeq4 = row['系统名称属性']
        currentSeq7 = row['部件名称属性']

        if currentSeq == "零件" and currentSeq1 != "外购":
            matched_value = get_matching_value(currentSeq4, currentSeq7, currentSeq2, equal_dict, like_dict)
            if matched_value:
                df.at[i, '新列'] = matched_value
            else:
                df.at[i, '新列'] = remove_non_chinese_or_roman(currentSeq2)
        else:
            df.at[i, '新列'] = row['部件名称属性']

    # 保存结果到新文件
    output_file = 'output.xlsx'
    df.to_excel(output_file, sheet_name='Sheet7', index=False)
    print(f"结果已保存到 {output_file}")

# 去除非汉字和罗马字母的字符
def remove_non_chinese_or_roman(text):
    return ''.join(filter(lambda x: u'\u4e00' <= x <= u'\u9fff' or 'A' <= x <= 'Z' or 'a' <= x <= 'z', text))

# 调用主逻辑
update_ming_chen_shu_xing_test('input.xlsx')
