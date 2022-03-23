


# f = open('data.txt','r',encoding='utf-8')
# #返回一个str
# # print(f.read())
# # print(type(f.read()))
# # print('一行行读取')
#
# #设置游标的位置
# # f.seek(0)
#
# #返回一个str，一次读取一行
# # print(f.readline())
# # print(type(f.readline()))
#
# #返回一个list，一次读取多行
# print(f.readlines())
# print(type(f.readlines()))
#
# f.close()

#这种写法会自动关闭文件
with open('data.txt','r',encoding='utf-8') as f:
    f.read()
    # f.readline()
    # f.readlines()
print(f.closed)