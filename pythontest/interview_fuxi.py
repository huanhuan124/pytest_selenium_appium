import json
import os.path
from itertools import permutations

import yaml


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
# before = '等等'
# after = 'ab'
# duiwei_replace2(before, after)

def merge_list(list1,list2):
    """
    #合并两个有序数组
    list1 = [1,2,4,6,10,11,12,13]
    list2 = [0,4,9]
    :param list1:
    :param list2:
    :return:
    """
    la = len(list1)
    lb = len(list2)
    i,j = 0,0
    res = []
    while i<la and j<lb :
        # print(i,j)
        if list1[i] < list2[j]:
            res.append(list1[i])
            i = i+1
        else:
            res.append(list2[j])
            j = j +1
    if i<la:
        for i in range(i,la):
            res.append(list1[i])
    if j<lb:
        for j in range(j,lb):
            res.append(list2[j])
    return res

# list1 = [1,2,4,6,10,11,12,13]
# list2 = [0,4,9]
# print(merge_list(list1, list2))





def find_min_inex(nums,n):
    """
        nums = [1,2,2,4,5]
        n = 2
        找出n在nums里面第一次出现时的下标
        :param nums:
        :param n:
        :return:
    """
    for i in range(len(nums)):
        if nums[i] == n:
            return i


def erfen_find_min_inex(nums,n):
    """
    nums = [1,2,2,4,5]
    n = 2
    找出n在nums里面第一次出现时的下标
    :param nums:
    :param n:
    :return:
    """
    l = 0
    r = len(nums)-1

    while l < r :
        middle = (l + r) // 2
        if n < nums[middle]:
            r = middle - 1
        elif n > nums[middle]:
            l = middle + 1
        else:
            #实现找到那个数，但是不一定是最小的下标
            # return middle
            # print(middle)
            # 实现找到那个数，并且是最小的下标
            for i in range(middle,-1,-1):
                # print(i)
                if nums[i] == nums[i-1]:
                    if i==0:
                        return 0
                    continue
                else:
                    return i
    else:
        return None


def hanshu_find_min_inde(nums,n):
    x = nums.count(n)
    # print(x)
    index = -1
    res = []
    for i in range(x):
        index = nums.index(n,index+1)
        res.append(index)
    print(res)
    return res[0]


# nums = [1,1,1,3,5,5,6]
# n = 1
# print(erfen_find_min_inex(nums, n))
# print(find_min_inex(nums, n))
# print(hanshu_find_min_inde(nums,n))


def quicksort(nums):
    """
        步骤:
        nums = [1,4,2,3,8]
        从数列中挑出一个元素，称为”基准”（pivot），
        重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
        递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

        :return:
        """
    less = []
    more = []
    middle = []
    n = len(nums)
    if n <= 1:
        return nums
    else:
        p = nums[0]
        for i in nums:
            if i < p:
                less.append(i)
            elif i > p:
                more.append(i)
            else:
                middle.append(i)
        less = quicksort(less)
        more = quicksort(more)

    return less + middle + more



# nums = [4,1,2,3,8]
# print(quicksort(nums))



def selectsort(lista):
    """
            步骤:
            在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
            再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
            重复第二步，直到所有元素均排序完毕。
            每一轮里面都设定第一个为最小数，然后一轮一轮比较，从他后面一个开始跟他比，如果有比他小的，跟他换位置，继续比，再遇到小的，就继续换位置
            :return:
    """
    # lista = [10, 5, 3, 9]
    print("排序前：", lista)
    n = len(lista)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if lista[j] < lista[min]:
                lista[j],lista[min] = lista[min],lista[j]

    print("排序后：", lista)


def maopaosort(nums):
    """

    :param nums:
    :return:
    """
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[j],nums[i] = nums[i],nums[j]
    return nums
# nums = [1,4,2,3,8]
# # print(maopaosort(nums))
# selectsort(nums)


def list_insert_new(arr,n):
    print("~~~~~~~~~~~~~~~~~~~把一个数字插入到有序数组中，使他仍然有序~~~~~~~~~~~~~~~~~~~~~~~~~")
    # 把一个数字插入到有序数组中，使他仍然有序
    # 注意：考虑数大于数组中的所有数的情况，此时，需要把数插入到数组的最后
    # insert(i,x) 在i的位置上插入x的值，后面的元素值向后移动
    # arr = [1, 3, 4, 6, 10]
    print(arr)
    for i in range(len(arr)):
        if n <= arr[i]:
            arr.insert(i,n)
            break
    if i == len(arr)-1:
        arr.insert(i+1,n)
    print(arr)


# arr = [1, 3, 3, 4, 6, 10]
# n = 11
# list_insert_new(arr,n)

def quicksort2(la):


    less = []
    more = []
    middle = []
    n = len(la)

    if n<=1:
        return la

    p= la[0]
    for i in la:
        if i < p:
            less.append(i)
        elif i > p:
            more.append(i)
        else:
            middle.append(i)
    less = quicksort2(less)
    more = quicksort2(more)
    return less+middle+more

# print('---快速排序---')
# la = [2,1,5,9,8]
# print(quicksort2(la))



def listcontaindict_sort(la):
    """
    请按照age或者name升序排序
    la = [{'name':'Lily','age':30},{'name':'Tom','age':20},{'name':'Jim','age':28}
      ,{'name':'Fish','age':22},{'name':'Rabbit','age':38}]
    输出：
    [{'name': 'Tom', 'age': 20}, {'name': 'Fish', 'age': 22}, {'name': 'Jim', 'age': 28}, {'name': 'Lily', 'age': 30}, {'name': 'Rabbit', 'age': 38}]
    :return:
    """
    # 快速排序
    # less = []
    # more = []
    # middle = []
    #
    # n = len(la)
    # if n<=1:
    #     return la
    #
    # p = la[0]['age']
    # print(p)
    # for x in la:
    #     if x['age'] < p:
    #         less.append(x)
    #     elif x['age'] >p:
    #         more.append(x)
    #     else:
    #         middle.append(x)
    # less = listcontaindict_sort(less)
    # more = listcontaindict_sort(more)
    #
    # return less+middle+more

#     冒泡排序
    for x in range(len(la)):
        for y in range(1,len(la)-x):
            if la[y]['age'] < la[y-1]['age']:
                la[y],la[y-1] = la[y-1],la[y]
        # print(la)
    return la


# la = [{'name':'Lily','age':30},{'name':'Tom','age':20},{'name':'Jim','age':48}
#       ,{'name':'Fish','age':22},{'name':'Rabbit','age':38}]
# print(listcontaindict_sort(la))


def count_file_content(filenamepath):
    # 统计一共有几行
    # 统计一共有多少个字符
    # 统计一个有多少个大写字母，数字，小写字母
    c = 0
    d = 0
    lowerc = 0
    uppperc = 0
    num = 0
    with open(filenamepath,'r') as f:
        for line in f:
            c = c+1
            # 需要去掉尾部的换行符
            for i in line.strip():
                print(i)
                d = d+1
                if i.isupper():
                    uppperc = uppperc + 1
                elif i.islower():
                    lowerc = lowerc + 1
                elif i.isdigit():
                    num = num + 1


    print(f"一共有{c}行")
    print(f"一共有{d}个字符")
    print(f"一共有{uppperc}个大写字母")
    print(f"一共有{lowerc}个小写字母")
    print(f"一共有{num}个数字")


# filename = 'test1.txt'
# filenamepath = os.path.abspath(__file__+f'/../data/{filename}')
# print(filenamepath)
# count_file_content(filenamepath)

def list_insert3(arr,n):
    """
    #把一个数字插入到有序数组中，使他仍然有序
    #注意：考虑数大于数组中的所有数的情况，此时，需要把数插入到数组的最后
    arr1 = [1, 3, 4, 6, 10]
    :return:
    """
    for i in range(len(arr)):
        if n <=arr[i]:
            arr.insert(i,n)
            break

    if i == len(arr)-1:
        arr.insert(i+1,n)
    print(arr)


arr = [1, 3, 4, 6, 10]
n = 10
list_insert3(arr,n)




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



# print("~~~~~~~~~~~~~~~~~~~~给定一个数字，利用二分查找，找出他在有序数组中的索引~~~~~~~~~~~~~~~~~~~~")
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


def remove_repeat_char_sort():
        """
        s = "ajldjljfd"，去重并从小到大排序输出"adfjl"
        :return:
        """

        s = "ajldjljfd"
        res = []
        for i in s:
            if i not in res:
                res.append(i)
        print(res)
        res.sort()
        print(res)
        resnew = ''.join(res)
        print(resnew)

# remove_repeat_char_sort()

def repeatchar():
        """
        找出数组中重复的数字
        在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
        :return:
        """
        arr = [1,2,2,3,3,3]
        repeatdic = {}

        for i in arr:
            repeatdic[i] = arr.count(i)

        print(repeatdic)
        return repeatdic

        # for i in arr:
        #     if i not in res:
        #         res.append(i)
        #     else:
        #         return i


# print(repeatchar())


def max_lianxu_one_num():
        """
        最大连续1的个数
        :return:
        """
        lista = [1, 1, 0, 1, 1, 1]
        maxcount = count =0
        for i in range(len(lista)):
            if lista[i] == 1:
                count = count +1
            else:
                maxcount = max(maxcount,count)
                count = 0
        maxcount = max(maxcount,count)
        print(maxcount)




def tongji_capital_char(filename):
    """
    统计文件中有多少个大写字符
    :return:
    """
    c,d,e = 0,0,0
    with open(filename,'r') as f:

        for line in f:
            print(line)
            for i in line.strip():
                e = e+1
                if i.isupper():
                    c = c +1
                if i.isdigit():
                    d = d+1
        print(f"总共有{e}个字符，数字有{d}个，大写字母有{c}个")
        if c+d == e:
            print("文件全部由大写字母和数字组成")
        else:
            print("文件不是全部由大写字母和数字组成")
        return c


# filename = os.path.abspath(__file__)+"/../data/test1.txt"
# filename = os.path.abspath(__file__)+"/../test2.txt"
# print(filename)
# print(tongji_capital_char(filename))
# # ord对应字符的acsii码
# print(ord('Z'))

def file_xiangguan(filename):
    """

    :param filename:
    :return:
    """
    # 读取文件
    # p_string = ''
    # with open(filename,'r') as f:
    #     # 返回一个列表，每行是一个元素
    #     lines = f.readlines()
    #     # print(lines)
    #     # print(type(lines))
    #     for line in lines:
    #         x = line.strip()
    #         p_string += x
    #     print(p_string)
    #
    #     c = 0
    #     for i in p_string:
    #         if i >= chr(65) and i<=chr(65+26):
    #             c = c+1
    #     return c

#  写文件
    with open(filename,'w') as f:
        f.write('12332')






# filename = "test2.txt"
# print(file_xiangguan(filename))


def file_yaml(filename):
    """

    :param filename:
    :return:
    """
    # 读取yaml文件中的内容
    with open(filename,'r') as f:
        x = yaml.safe_load(f)
        print(x)
        print(type(x))
    # 把内容写入到yaml文件中。    a追加，w覆盖写入
    with open(filename,'a') as f1:
        yaml.safe_dump('11111',f1)

# filename = "testyaml.yml"
# file_yaml(filename)

def json_file(filename):
    # 以json方式读取文件，文件中如果是json串必须用双引号
    with open(filename,'r') as f:
        x = json.load(f)
        print(x)
        print(type(x))

    # 把json串写入文件，如果是json串最好用双引号，虽然单引号也不报错
    data = {'name':'yiyi','age':12}
    with open(filename,'w') as f2:
        json.dump(data,f2)

# filename = "testjson.txt"
# json_file(filename)

def json_str():
    # json.dumps(data) 把dict转换为json字符串
    # data = {"name": "yiyi", "sex": "female","prename": "erer", "age": 20}
    # data = {'name': 'yiyi', 'sex': 'female', 'prename': 'erer', 'age': 20}
    # c = json.dumps(data)
    # print(c)
    # print(type(c))

    # 把字符串转为dict
    data = '{"name": "yiyi", "sex": "female", "prename": "erer", "age": 20}'
    dc = json.loads(data)
    print(dc)
    print(type(dc))
#
# json_str()

def list_dict_sort(lista):
    """
    一个列表中包含多个字典，根据age的值排序
    lista = [{'name':'Homer','age':39},{'name':'Bart','age':10}]
    :param lista:
    :return:
    """
    # lista = [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 90},
    #         {'name': 'Jim', 'age': 70}, {'name': 'Tom', 'age': 80}]
    # print(lista)
    # # 按照name升序排序，倒序需要加参数reverse=True
    # list_name = sorted(lista,key=lambda x:x['name'],reverse=True)
    # print(list_name)
    # #     按照age排序
    # list_age = sorted(lista,key=lambda x:x['age'])
    # print(list_age)

    # #     快速排序，按照age的升序排序，如果按照name排序，就把age改成name
    # if len(lista)==0:
    #     return []
    # elif len(lista)==1:
    #     return lista
    #
    # mid = lista[0]['age']
    # left =[]
    # right = []
    # for x in lista[1:]:
    #     print(x)
    #     if x['age'] < mid:
    #         left.append(x)
    #     else:
    #         right.append(x)
    # return list_dict_sort(left) + [lista[0]] + list_dict_sort(right)

    # 快速排序，按照age的升序排序，如果按照name排序，就把age改成name
    # left = []
    # right = []
    # mid = []
    # n = len(lista)
    # if n <= 1:
    #     return lista
    # else:
    #     p = lista[0]['name']
    #     print(p)
    #     for x in lista:
    #         print(x)
    #         if x['name'] < p:
    #             left.append(x)
    #         elif x['name']>p:
    #             right.append(x)
    #         else:
    #             mid.append(x)
    #     left = list_dict_sort(left)
    #     right = list_dict_sort(right)
    # return left + mid + right

    # 冒泡排序，按照age的升序排序，如果按照name排序，就把age改成name
    # n = len(lista)
    # for i in range(n):
    #     for j in range(1,n-i):
    #         if lista[j-1]['age'] > lista[j]['age']:
    #             lista[j - 1],lista[j] = lista[j],lista[j - 1]
    # return lista

    # 选择排序，按照age的升序排序，如果按照name排序，就把age改成name
    # n = len(lista)
    # for i in range(n):
    #     min = i
    #     for j in range(i+1,n):
    #         if lista[j]['age'] < lista[min]['age']:
    #             lista[j],lista[min] = lista[min],lista[j]
    # return lista


    # print(lista)
    # # 按照age值排序
    # listnew = sorted(lista, key=lambda x: x['age'])
    # # 按照age值排序
    # listnew = sorted(lista, key=lambda x: x['name'])
    # print(listnew)
    # print(lista)
    #
    # s = {'f':1,'e':3,'a':0,'d':1}
    # skey = sorted(s.items(),key=lambda  x:x[0])
    # svalue = sorted(s.items(),key=lambda x:x[1])
    # print(skey)
    # print(svalue)

#     快速排序

    # less =[]
    # more =[]
    # middle =[]
    # n = len(lista)
    #
    # if n<=1:
    #     return lista
    # else:
    #     p = lista[0]['age']
    #     for x in lista:
    #         if x['age']<p:
    #             less.append(x)
    #         elif x['age'] > p:
    #             more.append(x)
    #         else:
    #             middle.append(x)
    #     less = list_dict_sort(less)
    #     more = list_dict_sort(more)
    # return less+middle+more

# #     冒泡排序
#     for i in range(len(lista)):
#         for j in range(1,len(lista)-i):
#             if lista[j-1]['age'] > lista[j]['age']:
#                 lista[j-1],lista[j] = lista[j],lista[j-1]
#     return lista

#     选择排序

    # for i in range(len(lista)):
    #     min = i
    #     for j in range(i+1,len(lista)):
    #         if lista[j]['age']<lista[min]['age']:
    #             lista[j],lista[min] = lista[min],lista[j]
    # return lista







def dictionairy():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[10] = 2
    key_value[5] = 12
    key_value[8] = 24
    key_value[6] = 18
    key_value[3] = 323
    # {2: 56, 10: 2, 5: 12, 8: 24, 6: 18, 3: 323}
    print(key_value)
    # print("按键(key)排序:")

    print(key_value.items())
    # 按键升序排列  [(2, 56), (3, 323), (5, 12), (6, 18), (8, 24), (10, 2)]
    print(sorted(key_value.items(), key=lambda asd: asd[0]))
    # 按值升序排列   [(10, 2), (5, 12), (6, 18), (8, 24), (2, 56), (3, 323)]
    print(sorted(key_value.items(), key=lambda asd: asd[1]))

    # 遍历字典
    for k in key_value.keys():
        print(k)
    for v in key_value.values():
        print(v)
    for k,v in key_value.items():
        print(k,v)


    print("====字典中包含字典")
    # 字典中再包含字典
    a = {'a': {'val': 3}, 'f': {'val': 4}, 'c': {'val': 1}, 'd': {'val2': 0}}
    print(a)
    # 按照字典的值排序
    print(sorted(a.items(), key=lambda asd: asd[1].get('val',0)))








    # sorted(key_value)
    # print(sorted(key_value))
    # print(key_value)
    # for i in sorted(key_value):
    #     print((i,key_value[i]))


# dictionairy()
lista = [{'name': 'Homer', 'age': 99}, {'name': 'Bart', 'age': 90},
            {'name': 'Jim', 'age': 70}, {'name': 'Tom', 'age': 80}]
# print(list_dict_sort(lista))


def two_list_trans():
    tl = [[1,2,3],[4,5,6]]
    tlen = len(tl)
    clen = len(tl[0])
    res = []
    for i in range(clen):
        m = []
        for j in range(tlen):
            m.append(tl[j][i])
        res.append(m)
    print(res)

# two_list_trans()

def dic_key_value_trans():
    """
    示例
    输入：{'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}，
    输出：{'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}
    :return:
    """
    dc = {'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}
    # print(dc['Ice'])
    dcnew = {}
    m=[]
    for k,v in dc.items():
        if dcnew.get(v):
            if type(dcnew.get(v)) == list:
                dcnew.get(v).append(k)
            else:
                m.append(dcnew.get(v))
                m.append(k)
                dcnew[v] = m

        else:
            dcnew[v] = k

    print(dcnew)

# dic_key_value_trans()

def dic_key_value_trans2():
    """
    输入：{'Cream': ['Ice', 'Light', 'Double'], '21': 'Age'}
    输出：{'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}
    :return:
    """
    dc = {'Cream': ['Ice', 'Light', 'Double'], '21': 'Age'}
    tempdic = {}
    for k,v in dc.items():
        # print(v)
        # print(dc.get(k))
        # print(isinstance(v, list))
        # isinstance(object, classinfo)
        if isinstance(v, list):
            for x in v:
                tempdic[x] = k
        else:
            tempdic[v] = k
    print(tempdic)

# dic_key_value_trans2()

def norepeat_max_zichuan():
    """
    abcb
    abcdefgccab

    给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

    示例 1:

    输入: s = "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    示例 2:

    输入: s = "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    示例 3:

    输入: s = "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

    请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
    示例 4:

    输入: s = ""
    输出: 0

    :return:
    """
    # 使用暴力破解算出无重复最长子串
    # s = "abcvde"

    # maxcount = 0
    # for i in range(len(s)):
    #     templist = []
    #     c = 0
    #     for j in range(i,len(s)):
    #         print('当前字符：'+s[j])
    #         if s[j] in templist:
    #             print('字符存在，结束内循环')
    #             break
    #         else:
    #             templist.append(s[j])
    #             c = c + 1
    #             print(templist,c)
    #
    #     maxcount = max(maxcount,c)
    # print(maxcount)

    # 利用滑动窗口，算出最大无重复最长子串
    ans = 0
    start = 0
    tempd = {}
    # s = "abcdccab"
    s = "pwwkew"
    for i ,c in enumerate(s):
        if c in tempd:
            start = max(start,tempd[c]+1)
            # start = tempd[c] + 1
            # print(f'当前start是：{start}')
        tempd[c] = i
        # print(i, c, start)
        ans = max(ans,i-start+1)
        # print(tempd)
        # print(f'当前最长无重复子串是：{ans}')
    return ans


# print('最长无重复子串')
# print(norepeat_max_zichuan())


def norepeat_max_zichuan_and_index():
    # s = "abcdccab"
    s = "pwwkew"
    # s = "bbb"
    # s = "abcd"
    dic = {}
    start,ans = 0,0
    left,right = 0,0
    for i,c in enumerate(s):
        if c in dic:
            start = max(start,dic[c]+1)
        dic[c]=i
        if ans<i-start+1:
            ans = i-start+1
            # left,right = start,i+1
            left,right = start,i
    return [ans,(left,right)]


# print(norepeat_max_zichuan_and_index())

def fun_emumerate():
    # tmplist = ['a','b','c','d']
    # for i,c in enumerate(tmplist):
    #     print(i,c)
    #
    filename = os.path.abspath(__file__)+"/../data/test1.txt"
    print(filename)
    count = 0
    # 统计文件中一共有多少行
    # for i ,c in enumerate(open(filename,'r')):
    #     print(i,c)
    #     count = count+1
    # print(count)

    # 统计文件中一共有多少行
    # count = len(open(filename,'r').readlines())
    # print(count)

    # 统计文件中一共有多少行
    with open(filename,'r') as f:
        for line in f:
            count = count+1
    print(count)

    # 把字符串的每个字符和下标对应的放到字典中
    s = 'abcdef'
    tmpd = {}
    for i,c in enumerate(s):
        # print(i,c)
        tmpd[c] = i
    print(tmpd)
    # if 'a' in tmpd.keys():
    if 'a' in tmpd:
        print('a在字典中')

# fun_emumerate()

def max_fivexianglianshu():
    """
    给定一个字符串格式的数字，请编写一个函数，找出所有5个相连数字中最大的数字。
    示例：
    输入： "1234567890"
    输出：67890
    :return:
    """

    s = "1234567890"
    s = "1234567898765"
    s = "731674765"
    maxnum = 0
    for i in range(len(s)-4):
        num = s[i:i+5]
        print(num)
        maxnum = max(maxnum,int(num))
    print(maxnum)

# max_fivexianglianshu()


def next_bigger():
    """
    给定一个正整数，请编写一个函数，将它的所有数字重新组合，找出刚好比它大一点儿的那个数字。
    实例：
    输入：12，返回：21
    输入：513，返回：531
    输入：144，返回：414
    题目难度：中等
    :return:
    """
    s = 513
    s = 144
    s = 12
    list_s = [i for i in str(s)]
    print(list_s)
    data = []
    for x in permutations(list_s):
        print(x)
        y = int(''.join(x))
        data.append(y)
    print(data)
    data.sort()
    print(data)

    for i in data:
        if s<i:
            print(i)
            return i









next_bigger()


# max_lianxu_one_num()


#         lista = [1,1,0,1,0,1]
#         maxcount = count = 0
#         n = len(lista)
#         for i in range(n):
#             if lista[i] == 1:
#                 count += 1
#             else:
#                 maxcount = max(maxcount,count)
#                 count = 0
#         maxcount = max(maxcount,count)
#         print("最大连续数是：",maxcount)






# c = [0, 1, 2, 4, 6, 9, 10, 13]
# print(c)
# d = 4
#
# result = find_by_middle2(c,0,len(c)-1,d)
# print(d,'在数组中的索引值是：',result)
#
# merge_list2()
# list_insert2()


# import os
#
#
# class Test_High_Frequency:
#
#     def test_os(self):
#         """
#         os.path.join()函数：连接两个或更多的路径名组件
#                1.如果各组件名首字母不包含’/’，则函数会自动加上    win  home\dev\
# 　　　　　　　　　2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃  win  /dev\
# 　　　　　　　　　3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾   win  home\dev\
#         os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
#     root 所指的是当前正在遍历的这个文件夹的本身的地址
#     dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
#     files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
#     topdown --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为true)。
#         :return:
#         """
#         path1 = 'home'
#         path2 = '/dev'
#         path3 = ''
#         path10 = path1+ path2 + path3
#         path20 = os.path.join(path1,path2,path3)
#         print(path10)
#         print(path20)
#         print(os.getcwd())
#
#         # for root, dirs, files in os.walk(".",topdown=False):
#         # E:\python_workspace\pytest_selenium_appium\pythontest\test1
#         for root, dirs, files in os.walk("E:\python_workspace\pytest_selenium_appium\pythontest\\test1", topdown=False):
#             print('root****'+ root)
#             print('dirs****' ,dirs)
#             print('files****' ,files)
#
#             for name in files:
#                 print(os.path.join(root,name))
#             for name in dirs:
#                 print(os.path.join(root,name))
#
#
#     def traverseFolder(self,path=""):
#         """
#         遍历实现文件夹中的文件
#         if 是文件夹：
#             if 不是空文件夹：
#                 开始遍历
#             else:
#                 是空文件夹
#         else:
#             不是文件夹，无法遍历
#         :return:
#         """
#
#         path = os.getcwd()
#         path = "E:\python_workspace\pytest_selenium_appium\pythontest2"
#         print(path)
#         if os.path.exists(path):
#             for root, dirs, files in os.walk(path):
#                 for name in dirs:
#                     print(os.path.join(root,name))
#                 for name in files:
#                     print(os.path.join(root,name))
#         else:
#             print("path 不存在")
#
#
#     def test_remove_sort(self):
#         """
#         s = "ajldjljfd"，去重并从小到大排序输出"adfjl"
#         :return:
#         """
#
#         s = "ajldjljfd"
#
#         # 方法1 去重连成字符串，然后转为list排序，再转为字符串
#         res = ''
#         #去重连成字符串
#         for i in range(len(s)):
#             if s[i] not in res:
#                 res = res+s[i]
#         print(res)
#         #字符串转换为列表
#         list_res = list(res)
#         print(list_res)
#         #列表正序排列
#         list_res.sort()
#         print(list_res)
#         #去重后倒序排列
#         # list_res.sort(reverse=True)
#         # print(list_res)
#         #列表转换为字符串
#         str_res = ''.join(list_res)
#         print(str_res)
#
#         #方法2 用set先去掉重复元素，然后转为list排序，再转为字符串
#         # s_set = set(s)
#         # print(s_set)
#         # s_list = list(s_set)
#         # s_list.sort()
#         # print(s_list)
#         # str_res = ''.join(s_list)
#         # print(str_res)
#
#     def test_remove_sort2(self):
#         """
#         s = "ajldjljfd"，去重并从小到大排序输出"adfjl"
#         :return:
#         """
#
#         s = "ajldjljfd"
#
#         # 方法1 去重连成字符串，然后转为list排序，再转为字符串
#         res = ''
#         #去重连成字符串
#         for i in range(len(s)):
#             if s[i] not in res:
#                 res = res+s[i]
#         print(res)
#
#
#     def test_samecharnum(self):
#         '''
#         需求：统计列表list1中元素3的个数，并返回每个元素的索引
#         list.count() 用于统计某个元素在列表中出现的次数。
#         list.index()  用于从列表中找出某个值第一个匹配项的索引位置。
#         :return:
#         '''
#         list1 = [3, 5, 8, 9, 2, 10, 6, 2, 8, 3, 4, 5, 5, 4, 1, 3, 9, 7, 10, 2]
#         count = list1.count(3)
#         print(count)
#         index_list = []
#         index = -1
#
#         # 通过list.index()方法的__start参数，指定起始索引
#         for i in range(0, count):
#             print('iiiiiiiiii',i)
#             print(index)
#             index = list1.index(3, index + 1)
#             print(index)
#             index_list.append(index)
#
#         print(index_list)
#
#     def test_samecharnum2(self):
#         list1 = [3, 5, 8, 9, 2, 10, 6, 2, 8, 3, 4, 5, 5, 4, 1, 3, 9, 7, 10, 2]
#         len_list = len(list1)
#         list_index = []
#         num = 0
#         for i in range(len_list):
#             if list1[i] == 3:
#                 num += 1
#                 list_index.append(i)
#         print(f"list1中3出现的次数是：{num}")
#         print("他的索引是：")
#         print(list_index)
#
#     def test_samcechar(self):
#         """
#         整数数组中只有一个元素出现了一次，其他元素都出现了2次或者更多次，找出这个只出现了一次的元素
#         :return:
#         """
#         list1 = [3, 5, 3, 9, 5, 5]
#         a = {}
#         for i in list1:
#             a[i] = list1.count(i)
#             # print(a)
#             if list1.count(i) == 1:
#                 print("只出现了一次的元素是：",i)
#         print(a)
#
#     def test_samcechar2(self):
#         """
#         整数数组中只有一个元素出现了一次，其他元素都出现了2次或者更多次，找出这个只出现了一次的元素
#         :return:
#         """
#         list1 = [3, 5, 3, 9, 5, 5]
#         num=0
#         dic={}
#         list1.sort()
#         print(list1)
#
#
#
#
#     def test_samchar3(self):
#         """
#         找出数组中重复的数字
#         在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#         :return:
#         """
#         nums = [1,2,3,1,1,2]
#         repeatdict = {}
#         for i in nums:
#             print(i)
#             if i not in repeatdict:
#                 repeatdict[i] = 1
#                 print('没有重复数')
#             else:
#                 print('重复数是',i)
#
#         print(repeatdict)
#
#
#
#
#
#
#
#
#
#     def test_max_lianxu_num(self):
#         """
#         最大连续1的个数
#         :return:
#         """
#         lista = [1,1,0,1,0,1]
#         maxcount = count = 0
#         n = len(lista)
#         for i in range(n):
#             if lista[i] == 1:
#                 count += 1
#             else:
#                 maxcount = max(maxcount,count)
#                 count = 0
#         maxcount = max(maxcount,count)
#         print("最大连续数是：",maxcount)
#
#
#     def test_max_lianxu_num2(self):
#         lista = [1,1,0,1,0,1,1,1]
#         maxcount = count = index = 0
#         n = len(lista)
#         while index < n:
#             if lista[index] == 1:
#                 count += 1
#             else:
#                 maxcount = max(maxcount,count)
#                 count = 0
#             index += 1
#
#         maxcount = max(maxcount,count)
#         print("最大连续数是：",maxcount)
#
