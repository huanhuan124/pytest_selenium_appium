#-*- coding: utf-8 -*-
'''
List�÷����ű�ʾ��������ļ��ϣ�����Ҫ����List�Ļ���ȻҪͨ�����������
������ӣ�ɾ��Ԫ�أ����Խ��и����滻
�����ٶ�����ռ���ڴ�С
��append()����������ݵ�β����pop()����ɾ�����һ��Ԫ��
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


#extend ��ls���ݵ�������Ԫ�طŵ�ls��[1,2,'p',23]
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



