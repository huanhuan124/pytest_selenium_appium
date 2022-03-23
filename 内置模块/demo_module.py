import os

# help(os)
# print(dir(os))

#获取系统名称
# print(os.name)
#获取系统环境变量信息
# print(os.environ)
#获取指定名称的环境变量信息
# print(os.getenv('PATH'))
#执行系统指令
# print(os.system('dir'))

print("------os目录-------")
#获取当前文件路径
print(os.getcwd())
#列出当前目录内的文件
print(os.listdir())
#创建目录
# os.mkdir('demotest')

print('------os路径---------')
#获取绝对路径
print(os.path.abspath('demo_module.py'))
#获取文件名
print(os.path.basename(os.path.abspath('demo_module.py')))
#获取文件路径

print(os.path.dirname(os.path.abspath('demo_module.py')))
#分割路径
print(os.path.split(os.path.abspath('demo_module.py')))
print(os.path.split(os.path.abspath('demo_module.py'))[1])
#判断路径是否存在
print(os.path.exists(os.path.abspath('demo_module.py')))
#判断是否是目录
print(os.path.isdir(os.path.split(os.path.abspath('demo_module.py'))[0]))
#判断是否是文件
print(os.path.isfile(os.path.split(os.path.abspath('demo_module.py'))[1]))
#获取文件大小
print(os.path.getsize(os.path.split(os.path.abspath('demo_module.py'))[1]))