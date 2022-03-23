import os

class OsDir:
    fileNum = 0
    dirNum = 0



    def traverseFolder(self,path):

        """
        os.listdir()
        ===》从上到下，遍历文件夹（文件夹中的文件夹和文件）和文件
        遍历实现文件夹中的文件
        if 路径存在：
            列出所有文件夹中的文件和文件夹并打印
            if 是文件夹
                遍历
        else:
            路径不存在
        :return:
        """

        # path = os.getcwd()
        # print('-------------',path)

        if os.path.exists(path):
            for name in os.listdir(path):
                name_dir = os.path.join(path, name)
                print(name_dir)
                if os.path.isfile(name_dir):
                    self.fileNum += 1
                if os.path.isdir(name_dir):
                    self.dirNum += 1
                    self.traverseFolder(name_dir)
            print(f'{path}中有文件{self.fileNum}个，文件夹{self.dirNum}个')
        else:
            print("path 不存在")


    def traverseFolder2(self, path):
        """
        os.walk()
        ===》先列出第一层的文件和文件夹，然后再遍历每个文件夹中的内容
        遍历实现文件夹中的文件
        if 路径存在：
            遍历文件夹并打印
            遍历文件并打印
        else:
            路径不存在
        :return:
        """
        fileNum = 0
        dirNum = 0
        # path = os.getcwd()
        # path = "E:\python_workspace\pytest_selenium_appium\pythontest2"
        # print(path)
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for name in dirs:
                    print(os.path.join(root, name))

                    dirNum += 1
                for name in files:
                    print(os.path.join(root, name))
                    fileNum += 1


        else:
            print("path 不存在")

        print(f'{path}中有文件{fileNum}个，文件夹{dirNum}个')

    def deleteDir(self,path):
        if os.path.exists(path):
            for name in os.listdir(path):
                namedir = os.path.join(path,name)

                if os.path.isdir(namedir):
                    print('当前路径------', namedir,'准备删除文件夹')

                    self.deleteDir(namedir)
                    #只能删除空目录
                    os.rmdir(namedir)
                else:
                    print('当前路径------', namedir,'准备删除文件')
                    #删除文件
                    os.remove(namedir)

        else:
            print(f'{path}不存在')

    def deleteDir2(self, path):
        if os.path.exists(path):
            #root 去掉当前文件名的当前路径，dirs文件夹，files文件
            for root, dirs, files in os.walk(path):
                for name in files:
                    namedir = os.path.join(root,name)
                    print("准备删除当前文件",namedir)
                    os.remove(namedir)
                for name in dirs:
                    namedir = os.path.join(root, name)
                    print("准备删除当前文件夹",namedir)
                    self.deleteDir2(namedir)
                    os.rmdir(namedir)

        else:
            print("path 不存在")



path = 'E:\项目文档\\2022\\test'
ostest = OsDir()
# ostest.traverseFolder(os.getcwd())
# ostest.traverseFolder(path)
# print("========================================")
# # ostest.traverseFolder2(os.getcwd())
# ostest.traverseFolder2(path)
#
# print("========================================")
# ostest.deleteDir(path)
print(os.getcwd())
print(os.path.dirname(os.path.realpath('__file__')))
print(os.path.dirname(os.path.abspath('__file__')))
