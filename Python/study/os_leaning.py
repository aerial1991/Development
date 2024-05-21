# os模块是Python标准库中整理文件和目录最为常用的模块，该模块提供了非常丰富的方法用来处理文件和目录。
import os

# 获取当前目录
print(os.getcwd())
# 获取当前目录下的所有文件
print(os.listdir('.'))
#传入任意一个path路径，深层次遍历指定路径下的所有子文件夹；
for root, dirs, files in os.walk('.'):
    print(root, dirs, files)
#传入一个path路径，判断指定路径下的目录是否存在。存在返回True，否则返回False。
print(os.path.exists('.'))
#传入一个path路径，创建单层(单个)文件夹；
os.mkdir('test')
#传入一个path路径，创建多层(多个)文件夹；
os.mkdirs('test/test1/test2')
#传入一个path路径，删除单层(单个)文件夹；
os.rmdir('test')
#传入一个path路径，删除多层(多个)文件夹；
os.rmdirs('test/test1/test2')
#传入一个路径，删除文件；
os.remove('test.txt')
#传入一个path路径，删除文件夹下的所有文件；
os.removes('test')
#传入两个path路径，将该路径拼接起来，形成一个新的完整路径；
os.path.join('test', 'test.txt')
#传入一个完整的path路径，将其拆分为绝对路径和文件名两个部分；将path分割成目录和文件名并以元组方式返回
os.path.split('test/test.txt')
#传入一个path路径，获取该路径的文件名；
os.path.basename('test/test.txt')
#传入一个path路径，获取该路径的目录名；
os.path.dirname('test/test.txt')
#传入一个path路径，获取该路径的文件后缀名；
os.path.splitext('test/test.txt')
#传入一个path路径，获取该路径的文件大小；
os.path.getsize('test/test.txt')
#返回当前操作系统的路径分隔符；
os.path.sep
#返回path的绝对路径，os.path.abspath（）取决于os.getcwd（）
os.path.abspath('test/test.txt')


