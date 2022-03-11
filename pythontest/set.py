#-*- coding: utf-8 -*-
'''
set 是无序的
不重复的
类似于一个list
通过set()方法创建
如果我们要判断一个元素是否在一些不同的条件内符合，用set是最好的选择
通过add和remove来添加、删除元素（保持不重复）
'''
import os

s_a = set([1,'r',2])
s_b = set([3,'f',1])
s1 = set('qirise') #set(['q','i','s','r','e'])
print(s1)
print(s_a)
print(1 in s_a)
print(s_a & s_b)
print(s_a | s_b)

s1.add(4)
print(s1)

s1.remove('e')
print(s1)

test = 'i'

if test in s1:
	print('true')
else:
	print('false')

