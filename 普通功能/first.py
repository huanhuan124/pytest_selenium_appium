__author__ = 'zenghuan'

a = 1
print(a)

str_a = """
this is a string
这是一串字符串
"""
print(str_a)
print("hogwarts \\n霍格沃兹")

print("shenzhou is a %d" % 123)

str_b = "  hogwarts is a {}{}  "

print(str_b.format("very good ","school"))

print( '+'.join("hello"))

print(str_a.replace("t","p"))

t = ['a','b','c']
print("".join(t))


str_c = "   hello  fun "
print(str_c.rstrip())

print(1!=2)

a,b = 1,1
print(id(a),id(b))
#is 判断内存地址是否一样
print(a == b)
print(a is b)
print(1 is 1.0)