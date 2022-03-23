#列表
# li = [2]
# print(li*5)
# li1 = [1,2,3]
# li2 = [4,5,6]
# # print(li1+li2)
#
# li1.extend(li2)
# print(li1)
#
# # li1.append(li2)
# # print(li1)
# li1.extend("hogwarts")
# print(li1)
#
# result2 = [[3]*(i+1) for i in range(3)]
# print(result2)
#
# #列表推导式
# #以列表显示1-10之间偶数的平方
# result = [i**2 for i in range(1,11) if i%2 == 0 ]
# print(result)
#
# #元组
# t = 1,2,3
# print(type(t),t)
#
# t1 = tuple("hogwarts")
# print(t1)
#
# a,b,c = t
# print(a,b,c)
#
# print(t1.index("o"))

#set 集合
# set1 = {i for i in range(1,5)}
# print(set1)
#
# set2 = {7,8,9,1}

# set1.add("zero")
# print(set1)
# set1.pop()
# print(set1)

# #集合的交集
# print(set1&set2)
# print(set1.intersection(set2))
# #集合的并集
# print(set1|set2)
# print(set1.union(set2))
# #集合的差集
# #存在集合set1，不存在set2的值
# print(set1-set2)
# print(set1.difference(set2))
#
# #字典
d1 = {"name":"test", "age":20}
print(d1,type(d1))

d1["from"] = "beijing"
d1["name"] = "dev"
print(d1)

# d2 = dict([("name","test"),("age",20)])
# print(d2,type(d2))
#
#
#
# #字典推导式
# d3= {k:v for k,v in [("name","test"),("age",20)]}
# print(d3)
