
def kuohaopiei(x):
    '''
        括号匹配
        输入的字符串中包含()，将他们进行匹配
        x = "(()"  false
        x = "(())"  true
        x = "(()))"  false
        x = ")))((("  false
        x = "(" false
        x = ")"  false
        :param x:
        :return:
    '''

    n = 0
    if len(x) == 1:
        return False
    for i in x:
        if i == '(':
            n = n + 1
        else:
            n = n - 1
        #说明右边先出的或者右边比左边多，直接是false
        if n < 0:
            return False
    #全部配对成功
    if n == 0:
        return True
    #配对失败，左边多或者右边多
    else:
        return False

# x = "(()"
# x = "(())"
# x = "(()))"
# x = ")))((("
# x = "("
# x = ")"
# x = "))"
# print(kuohaopiei(x))

def morekuohaopipei(x):
    """
        括号匹配
        输入的字符串中包含{}[]()，将他们进行匹配
        x = "{[]})"  false
        x = "{[}})"  false
        x = "([{}])"  true
        x = "({[]}"  false
        x = "}])([{"  false
        x = "[{(" false
        x = "]})"  false
        :return:
    """
    res = []
    for i in x:
        if i == '(' or i == '[' or i=='{':
            res.append(i)
        elif i == ')' or i == ']' or i=='}':
            #左边被匹配完了，或者没有出现左边的，就出现了右边的
            if len(res) == 0:
                return False
            #返回最后一个元素，且列表删除了最后的那个元素
            m = res.pop()
            #配对成功
            if (m == '(' and i == ')') or (m == '[' and i == ']') or (m == '{' and i == '}'):
                continue
            #配对不成功
            return False
    #左边还剩下多的
    if len(res) > 0:
        return False
    return True

# x = "{[]})"
# x = "{[}})"
# # x = "([{}])"
# x = "({[]}"
# x = "}])([{"
# x = "[{("
# x = "]})"
# print(morekuohaopipei(x))

def find_zichuan(str):
    """
    给定一个非空的字符串s，请编写一个函数，检查它是否可以通过由它的一个子串重复多次构成。
    备注：s由纯小写英文字母组成；多次指大于等于2次。
    示例：
    输入：“abab”
    输出：True
    解释：可以由子串 “ab" 重复两次构成
    :param str:
    :return:
    """
    for i in range(len(str)//2):
        print(str[0:i + 1])
        # print('----')
        if str[0:i+1] * (len(str)//(i+1)) == str:
            # print('1111')
            return True
    return False




# str = "aaa"
# str = "abab"
# str = "a"
# print(find_zichuan(str))

def find_min_zichuan(str):
    """
    给定一个非空字符串words，只包含纯小写字母。请编写一个函数，找出其中最短的一个子字符串，以及它重复的最大次数。

    示例：
    输入： ababab，输出： ("ab", 3)。
    输入：abcde，输出：("abcde", 1)。
    :param str:
    :return:
    """
    for i in range(len(str)):
        check = str[:i+1]
        if check * (len(str)//(i+1)) == str:
            return [check,len(str)//(i+1)]


# str = 'abababad'
# # str = 'abcde'
# print(find_min_zichuan(str))

def fib_recur(n):
    """
    斐波纳契数列以如下被以递归的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
    指的是这样一个数列：1、1、2、3、5、8、13、21、34
    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return 1

    return fib_recur(n-1) + fib_recur(n-2)

def  fib2(n):
    # 输出第N个斐波拉契数列
    a,b =1,1
    for i in range(n-1):
        # #a, b = b, a + b这里不能写成 a=b   b=a+b，如果写成这样，b就不是前两位相加的值，而是已经被b赋过值的a和b相加的值
        a,b = b,a+b

    return a

def fib_list(n):
    # 计算出n的斐波拉契数列中偶数的和
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    res = [1,1]
    for i in range(2,n):
        res.append((res[-1])+res[-2])
    # return res
    print(res)
    result = sum([j for j in res if j%2 == 0])
    # print(result)
    return result

#
# n=1
# n=2
# n=3
# n =9
# print(fib_recur(n))
# print(fib2(n))
# # 指的是这样一个数列：1、1、2、3、5、8、13、21、34
# print(fib_list(9))

def sum_of_digits(num):
    """
    给定一个正整数，请编写一个python函数，将它的字面数字进行累加总和，并列出算式。例如1234 ，那么返回1 + 2 + 3 + 4 = 10 。
    :param num:
    :return:
    """
    if num<10:
        return num

    return sum([int(i) for i in str(num)])
# num =1234
# print(sum_of_digits(num))

def two_max_num(nums):
    """
    给定一个数字列表，请编写一个函数，找出其中最大的两个不同数字，并且返回结果按照从大到小排列。

    示例：
    输入： [4, 10, 10, 9]，输出：[10, 9]
    :param nums:
    :return:
    """
    # lnum = list(set(nums))
    # lnum.sort(reverse=True)
    # return lnum[:2]

    res = []
    for i in nums:
        if i not in res:
            res.append(i)
    res.sort(reverse=True)
    return res[:2]


# nums = [4, 10, 10, 9]
# print(two_max_num(nums))

def get_nums_index(nums,target):
    """
    题目：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
    补充说明：
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
    你可以按任意顺序返回答案。
    示例：
    输入：nums = [2,7,11,15], target = 9
    输出：[0,1]
    """
    # for i in range(len(nums)):
    #     s = target - nums[i]
    #     if s in nums:
    #         s_index = nums.index(s)
    #         return [i,s_index]


    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


# nums = [2,7,11,15,7]
# target = 18
# print(get_nums_index(nums, target))

def same_diff(nums1,nums2):
    """
    nums1=[6,1,1,2,3]
    nums2=[1,4,2,4,5]
    '''
    结果1：
    相同元素：[1,2]
    不同元素：[6,3,4,5]
    :param nums1:
    :param nums2:
    :return:
    """

    same = list(set(nums1)&set(nums2))
    diff = list(set(nums1)^set(nums2))
    return same,diff

# nums1=[6,1,1,2,3]
# nums2=[1,4,2,4,5]
# print(same_diff(nums1, nums2))

def two_array_reverse(arr):
    """
    二维数组转换
    将[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    转换为：[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    :return:
    """
    h = len(arr)
    c = len(arr[0])
    res = []
    for i in range(c):
        m = []
        # 转换为[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
        # for j in range(h):
        # 转换为[[9, 5, 1], [10, 6, 2], [11, 7, 3], [12, 8, 4]]
        for j in range(h-1,-1,-1):
            m.append(arr[j][i])
        res.append(m)
    return res

# arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(two_array_reverse(arr))


def alp_martix(n):
    """
    我们今天的任务是，编写一个函数，接收一个数字n，返回一个由英文字母组成的 n*n 方阵。

    示例：
    输入：4
    输出：

    a b c d
    b c d e
    c d e f
    d e f g
    :return:
    """
    x = 97
    res = []
    for i in range(n):
        m = []
        for j in range(n):
            m.append(chr(x+j))
        print(m)
        x = x+1
        res.append(m)
    return res

# n=4
# print(alp_martix(n))

def list_reverse(list_num):
    """
    list反转
    :param list_num:
    :return:
    """
    # return list_num[::-1]
    for i in range(len(list_num)//2):
        list_num[i],list_num[-i-1] = list_num[-i-1],list_num[i]
    return list_num

# list_num = [1,2,3,4,5]
# print(list_reverse(list_num))


def remove_list(l1,l2):
    """
    给定两个数字列表，请编写一个函数，从第一个列表nums_a中移除所有在第二个列表nums_b中出现的元素，返回剩下元素组成的列表。

    【示例】
    输入：[1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3]
    输出：[2, 2, 4]
    解释：第一个列表剔除所有的数字1和3之后，最终剩下[2, 2, 4]
    :return:
    """
    # res = []
    # for i in l1:
    #     if i not in l2:
    #         res.append(i)
    #
    # return res

    for i in l2:
        while i in l1:
            l1.remove(i)
    return l1


# l1,l2 = [1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3]
# print(remove_list(l1, l2))

def huiwen(num):
    """
    回文是指一段数字或者文本，正着读和倒着读都是相同的，例如2002，110011都是回文数字。给定一个数字num，请编写一个函数，判断它是不是一个回文数字。

    【示例】
    输入：1221
    输出：True
    解释：1221倒过来依旧是1221，因此它是回文数字
    :param str:
    :return:
    """
    # if str(num) == str(num)[::-1]:
    #     return True
    # return False

    str_num = str(num)
    for i in range(len(str_num)//2):
        if str_num[i] != str_num[-i-1]:
            return False
    return True


# num  =110011
# print(huiwen(num))

def listadd_one(nums):
    """
    给定一个数字列表，其中每个元素都是正整数。请编写一个函数，将列表整体所代表的数字加1，然后返回成新列表。
    示例：
    输入：[2, 3, 9]，输出：[2, 4, 0]
    :param nums:
    :return:
    """

    ss =''
    for i in nums:
        ss = ss + str(i)
    print(ss)
    x = int(ss) + 1
    list_num = []
    for i in str(x):
        list_num.append(int(i))
    return list_num

# nums = [2,3,8]
# print(listadd_one(nums))

def max_xianlianshu(x):
    """
    给定一个字符串格式的数字，请编写一个函数，找出所有5个相连数字中最大的数字。

    示例：
    输入： "1234567890"
    输出：67890
    :param x:
    :return:
    """
    # max_num = 0
    # for i in range(len(x)):
    #     if int(x[i:i+5]) > max_num:
    #         max_num = int(x[i:i+5])
    # return max_num

    l = len(str(x))
    res = []
    if l >= 5:
        for i in range(l-4):
            res.append(int(str(x)[i:i+5]))
        return max(res)


# x = "9123"
# print(max_xianlianshu(x))


def dict_duidiao(dc):
    """
    给定一个键值都是字符串的字典，请编写一个函数，将原来的键和值进行对调。

    示例
    输入：{'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}，
    输出：{'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}
    :param dc:
    :return:
    """
    temp_dict = {}
    for k,v in dc.items():
        if temp_dict.get(v):
            # 第三次出现，细节存入数组中
            if type(temp_dict.get(v)) == list:
                temp_dict.get(v).append(k)
            else:
                #第二次出现，把第一次的值和第二次的值都存到列表中
                res = []
                res.append(temp_dict.get(v))
                res.append(k)
                temp_dict[v] = res
        else:
            #第一次出现直接存储
            temp_dict[v] = k
    return temp_dict

# dc = {'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}
# # dc = {'Ice': 'Cream', 'Age': '21'}
# print(dict_duidiao(dc))

def duiwei_replace2(before,after):
    """
    给定一段文本words：“天_青_色_等_烟_雨,_而_我_在_等_你”，请编写一个函数，接收两个文字一一对应的字符串 sentence1 和 sentence2，请把words中的与sentence1的相同汉字换成sentence2对应的汉字。

    示例：
    输入：sentence1 = “天青色等烟雨”，sentence2 = “炊烟袅袅升起”，
    输出：“炊_烟_袅_袅_升_起,_而_我_在_袅_你”
    输入："_", "欢"
    输出：“天欢青欢色欢等欢烟欢雨,欢而欢我欢在欢等欢你”
    :param before:
    :param after:
    :return:
    """
    words = "天_青_色_等_烟_雨,_而_我_在_等_你"
    list_words = list(words)
    for i in range(len(list_words)):
        for j in range(len(before)):
            if list_words[i] == before[j]:
                print(list_words[i], before[j], after[j])
                print("======")
                list_words[i] = after[j]
                # break
    words = ''.join(list_words)
    print(words)


#before = '天青色等烟雨'
#after = '炊烟袅袅升起'
before = '等等'
after = 'ab'
duiwei_replace2(before, after)

def merge_list(list1,list2):
    """
    合并两个有序数组
    :param list1:
    :param list2:
    :return:
    """

def erfen_find(nums,n):
    """
    nums = [1,2,2,4,5]
    n = 2
    找出n在nums里面第一次出现时的下标
    :param nums:
    :param n:
    :return:
    """
def quicksort(nums):
    """

    :param nums:
    :return:
    """

def selectsort(nums):
    """

    :param nums:
    :return:
    """
def maopaosort(nums):
    """

    :param nums:
    :return:
    """


def list_insert():
    print("~~~~~~~~~~~~~~~~~~~把一个数字插入到有序数组中，使他仍然有序~~~~~~~~~~~~~~~~~~~~~~~~~")
    #把一个数字插入到有序数组中，使他仍然有序
    #注意：考虑数大于数组中的所有数的情况，此时，需要把数插入到数组的最后
    arr1 = [1, 3, 4, 6, 10]
    print(arr1)
    x = 5
    print(x)
    arr3 = arr1.copy()			# 复制数组1
    i = 0
    while i < len(arr1):
        if x < arr1[i]:
            arr3.insert(i, x)
            break
        else:
            i += 1
    else:
        arr3.insert(i, x)
    print(arr3)

def list_insert2():
    print("~~~~~~~~~~~~~~~~~~~把一个数字插入到有序数组中，使他仍然有序~~~~~~~~~~~~~~~~~~~~~~~~~")
    #把一个数字插入到有序数组中，使他仍然有序
    #注意：考虑数大于数组中的所有数的情况，此时，需要把数插入到数组的最后
    arr1 = [1, 3, 4, 6, 10]
    print(arr1)
    x = 100
    print(x)
    arr3 = arr1.copy()			# 复制数组1
    print(len(arr1))
    for i in range(len(arr1)):
        if x <= arr1[i]:
            arr3.insert(i, x)
            break;
    print(i)
    if i == len(arr1)-1:
        arr3.insert(i+1,x)
    print(arr3)





def merge_list():
    print("~~~~~~~~~~~~~~~~~~~~合并两个有序数组~~~~~~~`~~~~~~~~~~~~~~")
    #合并两个有序数组
    a = [1,2,4,6,10,11,12,13]
    b = [0,4,9]
    print(a)
    print(b)

    i ,j = 0, 0
    c = []
    while i<len(a) and  j<len(b):
        # print(i, j)
        if a[i] < b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
        # print(i, j)

    #     print(c)
    # print(c)

    if i<len(a):
        for i in range(i,len(a)):
            c.append(a[i])
    else:
        for j in range(j, len(b)):
            c.append(b[j])
    print(c)

def merge_list2():
    print("~~~~~~~~~~~~~~~~~~~~合并两个有序数组~~~~~~~`~~~~~~~~~~~~~~")
    #合并两个有序数组
    a = [1,2,4]
    b = [0,4,9]
    print(a)
    print(b)

    i ,j = 0, 0
    c = []
    while i<len(a) or j<len(b):
        if i == len(a):
            c.append(b[j])
            j = j+1
        elif j == len(b):
            c.append(a[i])
            i = i+1
        elif a[i] < b[j]:
            c.append(a[i])
            i = i +1
        else:
            c.append(b[j])
            j = j+1
    #深拷贝，把c的内容全部赋值给A
    a[:] = c
    print(c)
    print(a)
    #
    # a[0] = 1
    # print(c)
    # print(a)



print("~~~~~~~~~~~~~~~~~~~~给定一个数字，利用二分查找，找出他在有序数组中的索引~~~~~~~~~~~~~~~~~~~~")
#查找一个元素在一个有序数组中的索引，利用递归
def find_by_middle(lista, left, right, x):
    middle = (left+right)//2
    print("中间值", middle)

    if left <= right:
        if x == lista[middle]:
            return middle
        elif x < lista[middle]:
            return find_by_middle(lista, left, middle-1, x)
        else:
            return find_by_middle(lista, middle + 1, right, x)

    return None


#查找一个元素在一个有序数组中的索引，不利用递归
def find_by_middle2(lista, left, right, x):
    while left <= right:
        #middle每次会变换
        middle = (left + right) // 2
        if lista[middle] == x:
            return middle
        elif x < lista[middle]:
            right = middle - 1
        else:
            left = middle + 1
    else:
        return None





# c = [0, 1, 2, 4, 6, 9, 10, 13]
# print(c)
# d = 4
#
# result = find_by_middle2(c,0,len(c)-1,d)
# print(d,'在数组中的索引值是：',result)
#
merge_list2()
list_insert2()


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
        print(os.getcwd())

        # for root, dirs, files in os.walk(".",topdown=False):
        # E:\python_workspace\pytest_selenium_appium\pythontest\test1
        for root, dirs, files in os.walk("E:\python_workspace\pytest_selenium_appium\pythontest\\test1", topdown=False):
            print('root****'+ root)
            print('dirs****' ,dirs)
            print('files****' ,files)

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
        res = ''
        #去重连成字符串
        for i in range(len(s)):
            if s[i] not in res:
                res = res+s[i]
        print(res)
        #字符串转换为列表
        list_res = list(res)
        print(list_res)
        #列表正序排列
        list_res.sort()
        print(list_res)
        #去重后倒序排列
        # list_res.sort(reverse=True)
        # print(list_res)
        #列表转换为字符串
        str_res = ''.join(list_res)
        print(str_res)

        #方法2 用set先去掉重复元素，然后转为list排序，再转为字符串
        # s_set = set(s)
        # print(s_set)
        # s_list = list(s_set)
        # s_list.sort()
        # print(s_list)
        # str_res = ''.join(s_list)
        # print(str_res)

    def test_remove_sort2(self):
        """
        s = "ajldjljfd"，去重并从小到大排序输出"adfjl"
        :return:
        """

        s = "ajldjljfd"

        # 方法1 去重连成字符串，然后转为list排序，再转为字符串
        res = ''
        #去重连成字符串
        for i in range(len(s)):
            if s[i] not in res:
                res = res+s[i]
        print(res)


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
            print(index)
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
            # print(a)
            if list1.count(i) == 1:
                print("只出现了一次的元素是：",i)
        print(a)

    def test_samcechar2(self):
        """
        整数数组中只有一个元素出现了一次，其他元素都出现了2次或者更多次，找出这个只出现了一次的元素
        :return:
        """
        list1 = [3, 5, 3, 9, 5, 5]
        num=0
        dic={}
        list1.sort()
        print(list1)




    def test_samchar3(self):
        """
        找出数组中重复的数字
        在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
        :return:
        """
        nums = [1,2,3,1,1,2]
        repeatdict = {}
        for i in nums:
            print(i)
            if i not in repeatdict:
                repeatdict[i] = 1
                print('没有重复数')
            else:
                print('重复数是',i)

        print(repeatdict)









    def test_max_lianxu_num(self):
        """
        最大连续1的个数
        :return:
        """
        lista = [1,1,0,1,0,1]
        maxcount = count = 0
        n = len(lista)
        for i in range(n):
            if lista[i] == 1:
                count += 1
            else:
                maxcount = max(maxcount,count)
                count = 0
        maxcount = max(maxcount,count)
        print("最大连续数是：",maxcount)


    def test_max_lianxu_num2(self):
        lista = [1,1,0,1,0,1,1,1]
        maxcount = count = index = 0
        n = len(lista)
        while index < n:
            if lista[index] == 1:
                count += 1
            else:
                maxcount = max(maxcount,count)
                count = 0
            index += 1

        maxcount = max(maxcount,count)
        print("最大连续数是：",maxcount)

