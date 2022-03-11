import os


class Test_High_Frequency:

    def test_os(self):
        """
        os.path.join()函数：连接两个或更多的路径名组件

               1.如果各组件名首字母不包含’/’，则函数会自动加上    win  home\dev\

　　　　　　　　　2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃  win  /dev\

　　　　　　　　　3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾   win  home\dev\

        os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。

    root 所指的是当前正在遍历的这个文件夹的本身的地址
    dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    topdown --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为true)。
        :return:
        """
        path1 = 'home'
        path2 = '/dev'
        path3 = ''
        path10 = path1+ path2 + path3
        path20 = os.path.join(path1,path2,path3)
        print(path10)
        print(path20)

        for root, dirs, files in os.walk(".",topdown=False):
            print('root****'+ root)
            for name in files:
                print(os.path.join(root,name))
            for name in dirs:
                print(os.path.join(root,name))


    def traverseFolder(self,path=""):
        """
        遍历实现文件夹中的文件
        if 是文件夹：
            if 不是空文件夹：
                开始遍历
            else:
                是空文件夹
        else:
            不是文件夹，无法遍历
        :return:
        """

        path = os.getcwd()
        path = "E:\python_workspace\pytest_selenium_appium\pythontest2"
        print(path)
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for name in dirs:
                    print(os.path.join(root,name))
                for name in files:
                    print(os.path.join(root,name))
        else:
            print("path 不存在")
