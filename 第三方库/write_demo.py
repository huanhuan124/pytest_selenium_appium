with open('data1.txt',mode='w+',encoding='utf-8') as f:
    f.write("这是一个写文件的功能")

print(f.closed)