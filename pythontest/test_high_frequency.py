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


    def test_remove_sort(self):
        """
        s = "ajldjljfd"，去重并从小到大排序输出"adfjl"
        :return:
        """

        s = "ajldjljfd"

        # 方法1 去重连成字符串，然后转为list排序，再转为字符串
        # res = ''
        # #去重连成字符串
        # for i in range(len(s)):
        #     if s[i] not in res:
        #         res = res+s[i]
        # print(res)
        # #字符串转换为列表
        # list_res = list(res)
        # print(list_res)
        # #列表正序排列
        # list_res.sort()
        # print(list_res)
        # #去重后倒序排列
        # # list_res.sort(reverse=True)
        # # print(list_res)
        # #列表转换为字符串
        # str_res = ''.join(list_res)
        # print(str_res)

        #方法2 用set先去掉重复元素，然后转为list排序，再转为字符串
        s_set = set(s)
        print(s_set)
        s_list = list(s_set)
        s_list.sort()
        print(s_list)
        str_res = ''.join(s_list)
        print(str_res)

        if  1==1:
            pass
        elif 1==2:
            pass
        else:
            pass


    def test_samecharnum(self):
        '''
        需求：统计列表list1中元素3的个数，并返回每个元素的索引
        list.count() 用于统计某个元素在列表中出现的次数。
        list.index()  用于从列表中找出某个值第一个匹配项的索引位置。
        :return:
        '''
        list1 = [3, 5, 8, 9, 2, 10, 6, 2, 8, 3, 4, 5, 5, 4, 1, 3, 9, 7, 10, 2]
        count = list1.count(3)
        print(count)
        index_list = []
        index = -1

        # 通过list.index()方法的__start参数，指定起始索引
        for i in range(0, count):
            print('iiiiiiiiii',i)
            index = list1.index(3, index + 1)
            print(index)
            index_list.append(index)

        print(index_list)

    def test_samecharnum2(self):
        list1 = [3, 5, 8, 9, 2, 10, 6, 2, 8, 3, 4, 5, 5, 4, 1, 3, 9, 7, 10, 2]
        len_list = len(list1)
        list_index = []
        num = 0
        for i in range(len_list):
            if list1[i] == 3:
                num += 1
                list_index.append(i)
        print(f"list1中3出现的次数是：{num}")
        print("他的索引是：")
        print(list_index)

    def test_samcechar(self):
        """
        整数数组中只有一个元素出现了一次，其他元素都出现了2次或者更多次，找出这个只出现了一次的元素
        :return:
        """
        list1 = [3, 5, 3, 9, 5, 5]
        a = {}
        for i in list1:
            a[i] = list1.count(i)
            if list1.count(i) == 1:
                print("只出现了一次的元素是：",i)
        print(a)

    def test_samcechar2(self):
        """
        整数数组中只有一个元素出现了一次，其他元素都出现了2次或者更多次，找出这个只出现了一次的元素
        :return:
        """
        list1 = [3, 5, 3, 9, 5, 5]
        list1_set = set(list1)
        print(list1_set)
        a = {}
        for i in list1_set:
            a[i] = list1.count(i)
            if list1.count(i) == 1:
                print("只出现了一次的元素是：",i)
        print(a)









































