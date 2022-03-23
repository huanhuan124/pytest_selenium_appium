try:
    a = int(input("请输入被除数:"))
    b = int(input("请输入除数:"))
    c = a / b
    print("相除后的结果为：", c)
except (ValueError, ArithmeticError):
    print("除数不能为0")
except :
    print("未知异常")

print("请继续")