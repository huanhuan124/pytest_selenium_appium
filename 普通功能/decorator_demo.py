

import datetime
import selenium
'''
功能：用装饰器的方法，实现函数执行的时间
第1步：定义一个装饰器外函数，外函数有一个形参为func，接受被装饰的函数对象，外函数的返回值固定格式为内函数对象
第2步：定义一个装饰器内函数，内函数内调用func()
第3步：定义一个被装饰函数
第3步：如果被装饰函数有参数，那么需要在内函数中加形参，以及在函数调用的时候加参数，即func()调用的时候要加跟内函数一样的参数。
如果写死一个参数，但是又无法确定被装饰函数的参数数量，这种写法就不行，会报错
所以把两个地方的参数全部换成不定长参数*args, **kwargs
'''
def timer(func):
    def inner(*args, **kwargs):
        start_time = datetime.datetime.now()
        print("进入内函数")
        func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f'函数的执行时间是：{end_time-start_time}')
    return inner

@timer
def student(name,age):
    print('打印学生信息')
    print(name)
    print(age)
@timer
def student2(name,age,gender):
    print('打印学生信息2')
    print(name)
    print(age)
    print(gender)

student('zhangsan', 11)
student2('lisi',20,'男')