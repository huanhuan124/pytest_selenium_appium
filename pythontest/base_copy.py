import copy

a = [1,[2,3]]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)



a.append(3)
# b[3] = 5
a[1].append(4)
"""
可变对象中
b 赋值，其实就是给a弄了个别名。内存地址和a一样，子对象的内存地址相同，子对象变化同步，其他变化同步
c 内存地址和a不一样，子对象的内存地址相同，子对象变化同步，其他变化不同步
d 内存地址和a不一样，子对象的内存地址不相同，子对象变化不同步，其他变化不同步
"""
print(a,id(a),id(a[1]))
print(b,id(b),id(b[1]))
print(c,id(c),id(c[1]))
print(d,id(d),id(d[1]))

f = 2
e = f
m = copy.copy(f)
n = copy.deepcopy(f)
g =2
f = 3
"""
不可变对象中，只要是相同的值，就会指向一个内存地址，一旦值不同，改变值的对象的内存地址就会变，其他不变
"""
print(f,e,m,n,g)
print(id(f),id(e),id(m),id(n),id(g))