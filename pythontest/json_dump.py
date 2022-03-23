import json
import os.path

# data = {'name':'test','shares':100,'price':542.23}
data =  [1,3,5,6,4]
#json.dumps把dict转换为字符串，返回的是一个json格式的字符串
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

#json.loads把字符串转换为dict
json2 = json.loads(json_str)
print(json2)
print(type(json2))

basedir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(basedir,'json_data.txt')
#json.dump把data 数据写入到文件中
with open(filename,'w') as f:
    json.dump(data,f)

#json.load把文件中的数据加载出来，返回的是一个dict，注意打开文件的时候
with open(filename,'r') as f2:
    numbers = json.load(f2)
    print(numbers)
    print(type(numbers))

