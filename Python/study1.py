import pandas as pd
def age_19to_20(a):
    return 19<=a<=20
s = pd.read_excel('D:/test.xlsx',index_col='ID',header=1,sheet_name='Sheet3')
s =s.loc[s['Age'].apply(age_19to_20)]
print(s)
print(s.columns)  #列名
print(s.shape)    #几行几列
print(s.head(1))  #前几行数据
print(s.tail(3))   #后几行数据
d = {'s':100,'y':200,'z':300}
s1 = pd.Series(d)
print(s1)
s1.to_excel('D:/test1.xlsx',sheet_name='test3')

s2 = pd.Series([1,2,3],index=[1,2,3])
print(s2)

students = pd.read_excel('D:/test.xlsx',index_col='ID',header=1,sheet_name='Students')
scores = pd.read_excel('D:/test.xlsx',index_col='ID',header=1,sheet_name='Scores')
print(scores)
print(students)
table =students.merge(scores,how='left',on ='ID').fillna(0)
table.Score = table.Score.astype(int)
print(table)
