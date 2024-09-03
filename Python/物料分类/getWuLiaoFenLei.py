import pandas as pd
import re
from tkinter import filedialog
# 选择一个文件
file_path = filedialog.askopenfilename(title='请选择一个Excel表', filetypes=[('Excel','.xls .xlsx'),('文本','.txt'),('All Files', '*')],initialdir='E:\\',multiple=True)


#拆名称规格尺寸等字段函数
def is_greek_letter(s):
    greek_letters = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω"
    return any(char in greek_letters for char in s)

def is_chinese_or_roman(s):
    pattern = re.compile(r"[\u4e00-\u9fa5ⅠⅡⅢⅣⅤⅥⅦⅧⅨ]")
    return bool(pattern.search(s))

def remove_non_chinese_or_roman(s):
    if not s:
        return s

    # 保留数字开头的字符序列
    pattern = re.compile(r"^\d+°?|\d+\.\d+°?|[^\u4e00-\u9fa5ⅠⅡⅢⅣⅤⅥⅦⅧⅨ]")
    filtered_chars = pattern.sub("", s)

    # 如果第一个字符序列是非汉字或罗马数字的字符（如数字+符号），则保留它
    if not is_chinese_or_roman(s[0]):
        return s[0] + filtered_chars
    else:
        return filtered_chars

def split_data(df):
    # 添加新列
    df['新型号'] = ''
    df['新规格'] = ''
    df['新名称'] = ''
    df['L值'] = ''
    df['直径'] = ''
    df['壁厚'] = ''

    for index, row in df.iterrows():
        cell_value = row['名称']
        model_part = ""
        spec_part = ""
        chinese_part = ""
        l_value = ""
        a_part = ""
        b_part = ""

        print(f"Processing row {index}: {cell_value}")  # 打印当前行信息

        # 匹配汉字、希腊字母、罗马数字、特殊字符和空格
        matches = re.findall(r"([\u4e00-\u9fa5]+|Φ\d+[××]?\d*(?:\.\d+)?|δ\d+|L=\d+[a-zA-Z]?|\d+×\d+×\d+|[Α-Ωα-ω]+|Ⅰ|Ⅱ|Ⅲ|Ⅳ|Ⅴ|Ⅵ|Ⅶ|Ⅷ|Ⅸ|№[^ ]+|[^\s]+|\s+)", cell_value)
        print(f"Matches found: {matches}")  # 打印匹配结果

        for match in matches:
            match = match.strip()
            if match:
                if "№" in match:
                    model_part += match + " "
                elif is_chinese_or_roman(match):
                    chinese_part += match + " "
                elif match.startswith("L="):
                    l_value = match[2:]
                    spec_part += match + " "
                elif re.match(r"\d+×\d+×\d+", match):  # 匹配 "30×50×100" 格式
                    spec_part += match + " "
                elif is_greek_letter(match) or "Φ" in match or "δ" in match:
                    spec_part += match + " "
                else:
                    spec_part += match + " "
        print(f"Model part: {model_part}")  # 打印型号部分
        print(f"Spec part: {spec_part}")    # 打印规格部分
        print(f"Chinese part: {chinese_part}")  # 打印名称部分
        # 处理 "ΦA×B" 格式
        match = re.search(r"Φ(\d+)[××](\d+(?:\.\d+)?)", cell_value)
        if match:
            a_part = match.group(1)
            b_part = match.group(2)
        else:
            # 处理 "ΦA" 格式
            match = re.search(r"Φ(\d+)", cell_value)
            if match:
                a_part = match.group(1)
        print(f"Diameter (A part): {a_part}")  # 打印直径部分
        print(f"Thickness (B part): {b_part}")  # 打印壁厚部分
        # 进一步处理 chinese_part, 去除非汉字和罗马数字的字符，并剔除“型”的末尾
        chinese_part = remove_non_chinese_or_roman(chinese_part).strip()
        if chinese_part.endswith("型"):
            chinese_part = chinese_part[:-1].strip()

        # 写入到对应列
        df.at[index, '新型号'] = model_part.strip()
        df.at[index, '新规格'] = spec_part.strip()
        df.at[index, '新名称'] = chinese_part.strip()
        df.at[index, 'L值'] = l_value.strip()
        df.at[index, '直径'] = a_part.strip()
        df.at[index, '壁厚'] = b_part.strip()

        # 最后打印出当前行的新数据
        print(f"New model: {df.at[index, '新型号']}")
        print(f"New spec: {df.at[index, '新规格']}")
        print(f"New name: {df.at[index, '新名称']}")
        print(f"L value: {df.at[index, 'L值']}")
        print(f"Diameter: {df.at[index, '直径']}")
        print(f"Thickness: {df.at[index, '壁厚']}")

    return df

#更新材料名称字段
def update_cai_liao(df):
    # 添加新列
    df['新材料名称'] = ''

    # 定义正则表达式
    reg_ex = re.compile(r"Φ\d+×\d+", re.IGNORECASE)  # 匹配ΦA×B的模式

    # 遍历每一行
    for i, row in df.iterrows():
        if row['零件部件'] == "零件":
            # 获取零件图号
            current_seq = str(row['规格']).strip()
            current_seq1 = str(row['执行标准']).strip()
            current_seq2 = str(row['材质']).strip()

            if current_seq.startswith("δ"):
                df.at[i, '新材料名称'] = "钢板"
            elif current_seq.startswith("∠"):
                df.at[i, '新材料名称'] = "角钢"
            elif current_seq.startswith("["):
                df.at[i, '新材料名称'] = "槽钢"
            elif current_seq.startswith("I") or current_seq.startswith("Ⅰ"):
                df.at[i, '新材料名称'] = "工字钢"
            elif current_seq.startswith("H"):
                df.at[i, '新材料名称'] = "H型钢"
            elif current_seq.startswith("1\""):
                df.at[i, '新材料名称'] = "钢管"
            elif current_seq.startswith("Φ"):
                if reg_ex.search(current_seq):
                    df.at[i, '新材料名称'] = "钢管"
                else:
                    df.at[i, '新材料名称'] = "圆钢"
            elif current_seq1 in ["NB/T47008", "JB/T9626"]:
                df.at[i, '新材料名称'] = "锻件"
            elif current_seq2.startswith("ZG"):
                df.at[i, '新材料名称'] = "铸造件"

            if pd.isna(row['材料名称']) or row['材料名称'].strip() == "":
                df.at[i, '材料名称'] = df.at[i, '新材料名称']

    return df

#给令号匹配系统字段
def determine_system(seq):
    if seq.startswith("1") and not seq.startswith(("10", "11", "12", "13", "14", "15")):
        return "锅筒部分"
    elif seq.startswith("2"):
        return "水冷系统"
    elif seq.startswith("3"):
        return "钢结构"
    elif seq.startswith("4"):
        return "炉墙部分"
    elif seq.startswith("5"):
        return "过热器"
    elif seq.startswith("6"):
        return "省煤器"
    elif seq.startswith("7"):
        return "空气预热器"
    elif seq.startswith("8"):
        return "燃烧循环部分"
    elif seq.startswith("9"):
        return "本体管路及附件"
    elif seq.startswith("10"):
        return "杂件及备品备件"
    elif seq.startswith("11"):
        return "再热器"
    elif seq.startswith("12"):
        return "低低温省煤器"
    elif seq.startswith("13"):
        return "锅炉电梯竖井"
    elif seq.startswith("14"):
        return "水煤空预器"
    elif seq.startswith("15"):
        return "辅机部分"
    return ""  # 默认返回空字符串

#根据序号在工作表中查找对应的父级名称
def get_name_value(seq_value, df):
    first_dash_position = seq_value.find('-')
    if first_dash_position != -1:
        second_dash_position = seq_value.find('-', first_dash_position + 1)
        if second_dash_position != -1:
            first_dash_segment = seq_value[:second_dash_position]
        else:
            #first_dash_segment = seq_value[:first_dash_position + len(seq_value[first_dash_position + 1:])]
            first_dash_segment = seq_value
    else:
        first_dash_segment = seq_value
        print(f"提取的段: {first_dash_segment}")

    # 在工作表中查找 first_dash_segment 对应的名称
    name_value = ""
    for j, row in df.iterrows():
        if row['序号'].strip() == first_dash_segment:
            name_value = row['新名称']
            break

    return name_value

# 读取规则表并将采购件规则分配到字典中
def load_rules(rules_df):
    like_dict = {}
    for _, row in rules_df.iterrows():
        component = row['名称']
        result_value = str(row['物料分类'])
        match_type = row['匹配类型']
        if match_type == 'like':
            add_to_dict(like_dict, component, result_value)
    return like_dict

# 读取规则表并将企标零件规则分配到字典中
def load_qblj_rules(rules_df_qblj):
    equal_dict = {}
    for _, row in rules_df_qblj.iterrows():
        component = row['图号']
        result_value = str(row['物料分类'])
        match_type = row['匹配类型']
        if match_type == '=':
            add_to_dict(equal_dict, component, result_value)
    return equal_dict

# 读取规则表并将工艺增加零件规则分配到字典中
def load_gylj_rules(rules_df_gylj):
    equal_dict = {}
    for _, row in rules_df_gylj.iterrows():
        component = row['材料名称']
        result_value = str(row['物料分类'])
        match_type = row['匹配类型']
        if match_type == '=':
            add_to_dict(equal_dict, component, result_value)
    return equal_dict

# 读取规则表并将零件规则分配到字典中
def load_lj_rules(rules_df_lj):
    equal_dict = {}
    for _, row in rules_df_lj.iterrows():
        component = row['材料名称']
        result_value = str(row['物料分类'])
        match_type = row['匹配类型']
        if match_type == '=':
            add_to_dict(equal_dict, component, result_value)
    return equal_dict

# 读取规则表并将企标部件规则分配到字典中
def load_qbbj_rules(rules_df_qbbj):
    like_dict_qbbj = {}
    for _, row in rules_df_qbbj.iterrows():
        component = row['图号']
        result_value = str(row['物料分类'])
        match_type = row['匹配类型']
        if match_type == '=':
            add_to_dict(like_dict_qbbj, component, result_value)
    return like_dict_qbbj

# 读取规则表并将国标件规则分配到字典中
def load_gbj_rules(rules_df_gbj):
    like_dict_gbj = {}
    for _, row in rules_df_gbj.iterrows():
        component = row['图号']
        result_value = str(row['物料分类'])
        match_type = row['匹配类型']
        if match_type == '=':
            add_to_dict(like_dict_gbj, component, result_value)
    return like_dict_gbj

# 读取规则表并将工艺部件规则分配到字典中
def load_gybj_rules(rules_df_gybj):
    like_dict_gybj = {}
    for _, row in rules_df_gybj.iterrows():
        component = row['名称']
        result_value = str(row['物料分类'])
        match_type = row['匹配类型']
        if match_type == 'like':
            add_to_dict(like_dict_gybj, component, result_value)
    return like_dict_gybj

# 读取规则表并将普通部件规则分配到字典中
def load_bj_rules(rules_bj_df):
    component_dict = {}
    for _, row in rules_bj_df.iterrows():
        system = row['系统']
        name = row['名称']
        result_value = str(row['物料分类'])
        match_type = row['匹配类型']

        if match_type == 'like':
            if system not in component_dict:
                component_dict[system] = []
            # 在该系统下添加名称和结果值的元组
            if match_type == 'like':
                component_dict[system].append((name, result_value))
    return component_dict

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

# 获取匹配普通部件的函数
def get_bj_matching_value(system, name_value, component_dict):
    if system in component_dict:
        # 按名称长度降序排序，优先匹配更长的名称
        sorted_patterns = sorted(component_dict[system], key=lambda x: len(x[0]), reverse=True)
        for name_pattern, result_value in sorted_patterns:
            # 使用正则表达式匹配
            if re.search(re.escape(name_pattern), name_value):
                return result_value

    # 如果未匹配到，返回空字符串
    return ""

# 主逻辑：读取Sheet并进行替换
def update_ming_chen_shu_xing_test(file_path):
    # 读取数据
    df = pd.read_excel(file_path, sheet_name='Sheet1',dtype=str)
    df = split_data(df)
    df = update_cai_liao(df)
    rules_df = pd.read_excel(file_path, sheet_name='采购件', dtype=str)
    rules_df_qblj = pd.read_excel(file_path, sheet_name='企标零件', dtype=str)
    rules_df_gylj = pd.read_excel(file_path, sheet_name='工艺增加零件', dtype=str)
    rules_df_lj = pd.read_excel(file_path, sheet_name='零件', dtype=str)
    rules_df_qbbj = pd.read_excel(file_path, sheet_name='企标部件', dtype=str)
    rules_df_gbj = pd.read_excel(file_path, sheet_name='国标件', dtype=str)
    rules_df_gybj = pd.read_excel(file_path, sheet_name='工艺增加部件', dtype=str)
    rules_df_bj = pd.read_excel(file_path, sheet_name='部件', dtype=str)

    # 确保列名没有前后空格
    df.columns = df.columns.str.strip()
    rules_df.columns = rules_df.columns.str.strip()
    rules_df_qblj.columns = rules_df_qblj.columns.str.strip()
    rules_df_gylj.columns = rules_df_gylj.columns.str.strip()
    rules_df_lj.columns = rules_df_lj.columns.str.strip()
    rules_df_qbbj.columns = rules_df_qbbj.columns.str.strip()
    rules_df_gbj.columns = rules_df_gbj.columns.str.strip()
    rules_df_gybj.columns = rules_df_gybj.columns.str.strip()
    rules_df_bj.columns = rules_df_bj.columns.str.strip()

    # 添加系统字段列
    df['系统'] = df['序号'].apply(determine_system)

    # 加载规则到字典
    like_dict = load_rules(rules_df)
    equal_dict_qblj=load_qblj_rules(rules_df_qblj)
    equal_dict_gylj=load_gylj_rules(rules_df_gylj)
    equal_dict_lj=load_lj_rules(rules_df_lj)
    like_dict_qbbj=load_qbbj_rules(rules_df_qbbj)
    like_dict_gbj=load_gbj_rules(rules_df_gbj)
    like_dict_gybj=load_gybj_rules(rules_df_gybj)
    component_dict=load_bj_rules(rules_df_bj)

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
        currentSeq2 = row['新名称']
        currentSeq3 = row['序号']
        currentSeq4 = row['流程']
        currentSeq5 = row['图号']
        currentSeq6 = row['材料名称']

        print(f"处理行 {i}:")
        print(f"  零件部件: {currentSeq}")
        print(f"  制造方式: {currentSeq1}")
        print(f"  新名称: {currentSeq2}")
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
        elif currentSeq=="零件":
            if currentSeq5[:5] == "Q/TGJ" or currentSeq5[:1] == "L":
                matched_value = get_matching_value( currentSeq5, equal_dict_qblj,match_type='=')
                print(f"  匹配值: {matched_value}")
                if matched_value:
                    df.at[i, '物料分类'] = matched_value
                else:
                    df.at[i, '物料分类'] = ""
            elif currentSeq5[:2] == "TY":
                matched_value = get_matching_value( currentSeq6, equal_dict_gylj,match_type='=')
                print(f"  匹配值: {matched_value}")
                if matched_value:
                    df.at[i, '物料分类'] = matched_value
                else:
                    df.at[i, '物料分类'] = ""
            elif currentSeq5[:2] == "GB" or currentSeq5[:2] == "JB":
                matched_value = get_matching_value( currentSeq5, like_dict_gbj,match_type='=')
                print(f"  匹配值: {matched_value}")
                if matched_value:
                    df.at[i, '物料分类'] = matched_value
                else:
                    df.at[i, '物料分类'] = ""
            else:
                matched_value = get_matching_value( currentSeq6, equal_dict_lj,match_type='=')
                print(f"  匹配值: {matched_value}")
                if matched_value:
                    df.at[i, '物料分类'] = matched_value
                else:
                    df.at[i, '物料分类'] = ""
        elif currentSeq=="部件":
            if currentSeq5[:5] == "Q/TGJ" or currentSeq5[:1] == "L":
                matched_value = get_matching_value( currentSeq5, like_dict_qbbj,match_type='=')
                print(f"  匹配值: {matched_value}")
                if matched_value:
                    df.at[i, '物料分类'] = matched_value
                else:
                    df.at[i, '物料分类'] = ""
            elif currentSeq5[:2] == "TY" :
                matched_value = get_matching_value( currentSeq2, like_dict_gybj,match_type='like')
                print(f"  匹配值: {matched_value}")
                if matched_value:
                    df.at[i, '物料分类'] = matched_value
                else:
                    df.at[i, '物料分类'] = ""
            else :
            # 从 df 的对应列获取系统和名称
                system_value = row['系统']
                name_value = get_name_value(currentSeq3, df)
                print(f"  系统: {system_value}")
                print(f"  名称: {name_value}")
                matched_value = get_bj_matching_value(system_value,name_value, component_dict)
                print(f"  匹配值: {matched_value}")
                if matched_value:
                    df.at[i, '物料分类'] = matched_value
                else:
                    df.at[i, '物料分类'] = ""
    # 保存结果到新文件
    output_file = 'D:/output.xlsx'
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