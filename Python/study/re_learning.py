# re库是Python用来实现“正则表达式”的库，并且re库在Python中内置，无需使用pip安装

#正则表达式的英语：Regular Expression，编程语言中一般叫re或者regex
import re
# #compile()函数用来编译正则表达式，并返回正则表达式对象
# pattern = re.compile('[a-z]+')
# #findall()函数用来查找正则表达式的所有匹配
# result = pattern.findall()

text = '张三身高：178,体重：70kg,张三身高：180,体重：80kg'

print(re.findall(r'178', text))
print(re.findall(r'\d', text))    #\d表示单个数字
# re模块的方法:查找

search = re.search(r'张三', text)
print(search.group())

m =re.findall(r'张三', text)
print(m)

m1 = re.finditer(r'张三', text)
for i in m1:
    print(i.group())
#re模块的替换

m3=re.sub(r'张三', '***', text)
print(m3)
print('------------------------------')
#re模块的分割
m4=re.split(r'张三', text)
print(m4)
print('------------------------------')
pattern =re.compile(r'张三')
re1=pattern.findall(text)