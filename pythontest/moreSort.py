class MoreSort:

    def bubbleSort(self):
        """
        步骤
        冒泡排序算法的运作如下：
        比较相邻的元素。如果第一个比第二个大，就交换他们两个。
        对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
        针对所有的元素重复以上的步骤，除了最后一个。
        持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

        :return:
        """
        lista = [10, 5, 3, 9, 0, 1, 3]
        print("排序前：", lista)
        length = len(lista)
        #[0,length)
        #外层每个元素都要遍历一遍相邻两个元素的比较，一共length次数，从0开始
        for i in range(length):
            #里层从1开始，遍历的话，需要length-i,已经遍历过放到最后边的大数就不用再算了
            for j in range(1,length - i):
                if lista[j-1] > lista[j]:
                    lista[j-1], lista[j] = lista[j],lista[j-1]
        print("排序后：",lista)

    def selectionSort(self):
        """
        步骤:
        在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
        再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
        重复第二步，直到所有元素均排序完毕。
        :return:
        """
        lista = [10, 5, 3, 9]
        print("排序前：", lista)
        n = len(lista)
        for i in range(n):
            min = i
            print(min)
            for j in range(i+1,n):
                if lista[j] < lista[min]:
                    lista[j], lista[min] = lista[min], lista[j]
                print(lista)

        print("排序后：", lista)


    def quickSort(self,list):
        """
        步骤:
        从数列中挑出一个元素，称为”基准”（pivot），
        重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
        递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

        :return:
        """

        n = len(list)
        # print(n)
        less = []
        more = []
        middle = []
        if n<=1:
            # print("此列表不需要排序")
            return list
        else:
            p = list[0]
            for i in list:
                if i < p:
                    less.append(i)
                elif i > p:
                    more.append(i)
                else:
                    middle.append(i)
            less = self.quickSort(less)
            more = self.quickSort(more)

        return less+middle+more

    def mergelist(self):
        list1 = [0,1,2,3]
        list2 = [1,3,5]
        list3,list4 = [],[]
        dict4 = {}
        m = len(list1)
        n = len(list2)
        list1[m:] = list2

        list1.sort()
        print('排序后的拼接数组：',list1)

        # print(set(list1))
        for i in range(len(list1)):
            if list1[i] in list3:
                continue
            else:
                list3.append(list1[i])
        print('去重后的数组：',list3)
        #找出重复数=1 的元素和索引

        for j in list1:

            dict4[j] = list1.count(j)

        num = list1.count(3)
        index  = -1
        for j in range(0,num):
            index = list1.index(3,index+1)
            list4.append(index)
        print('每个元素出现的次数是：',dict4)
        print('元素3的索引是',list4)



lista = [10, 5, 3, 9, 0, 1, 3]
qs = MoreSort()
# #快速排序
# print("快速排序-----------")
# print("排序前：", lista)
# last_list = qs.quickSort(lista)
# print("排序后：",last_list)
#
# print("冒泡排序-----------")
# qs.bubbleSort()

# print("选择排序-----------")
# qs.selectionSort()
qs.mergelist()
