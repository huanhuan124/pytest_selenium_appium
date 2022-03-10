#-*- coding: utf-8 -*-
'''
List用方括号表示，是有序的集合，所以要访问List的话显然要通过序号来访问
可以添加，删除元素，可以进行复制替换
查找速度慢，占用内存小
用append()方法添加内容到尾部，pop()方法删除最后一个元素
'''
ls = [1,[1,2],'avc']
print ls
print ls[1]

for i in ls:
	print i
	

ls.append((4,5,6))
print ls
ls.append([11,22])
print ls


b = 56
ls.append(b)
print ls

c = ['p',23]
ls.append(c)  #[1,2,['p',23]]
print ls


#extend 把ls内容当作单个元素放到ls中[1,2,'p',23]
ls.extend(c)
print ls

x = 'abc'
print x
l = list(x)
print l
l[2]='E'
print l

str = '-'.join(l) #'a-b-E'
print str


y = [1,2,3,4,'a','b']
print y
y.pop()
print y

del(y[1])
print y

y.append('cdg')
print y
print 3 in y

xy = []
print xy
if not xy:
	print 1



