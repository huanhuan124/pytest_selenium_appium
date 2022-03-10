#-*- coding: utf-8 -*-

'''
无序
查找速度快，占内存
Key不可变，Value可变。一旦一个键值对加入dict后，它对应的key就不能再变了，但是Value是可以变化的。所以List不可以当做Dict的Key，但是可以作为Value
可以直接通过键值对方式添加dict中的元素
用key访问元素
key不能重复,value可以重复
使用dict[key]=value添加元素
使用pop(key)或者del(dict[key])删除元素
'''
d = {'bai':100,'q':1000,'g':1,'hao':100,'bai':10000}
print(d)

d['jone'] = 200
print(d)

print(d['bai'])

if 'q' in d:

	print(111)
	print(d.get('q'))

if 100 in d:
	print(100)
	
for k in d:
	print(str(k) + ':' + str(d[k]))
	
	
for k, v in d.items():
	print(str(k) + ':' + str(v))
	
print(d.keys())

d.pop('bai')
print(d)

d['lily'] = ['a',1]
print(d)

del(d['jone'])
print(d)

	
