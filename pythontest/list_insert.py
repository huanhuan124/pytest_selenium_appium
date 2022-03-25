# # 将一个数插入一个有序数组中，并使其仍然有序
# a = [10, 23, 24, 38, 46,]
# print("原始数组是：")
# for n in a:
#     print(n, end=" ")
# print()
# t = 0
#
# x = int(input("请输入整数:"))
#
# for i in range(len(a)):
#     print('iiiiiii',i)
#     if x < a[i]:
#         t = i
#         print('ttttttt',t)
#         break  # 循环结束时，i=5
# t = i  # 将循环结束时数组的下标赋值给t
# for j in range(len(a) - 1, t, -1):  # 数从后面依次后移直到遇到a[t]
#     print('jjjjjj', j)
#     a[j] = a[j - 1]
# a[t] = x
# print("插入新数后的数组是：")
# for n in a:
#     print(n, end=" ")  # 不换行输出，数字末尾是空格
# print()


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









