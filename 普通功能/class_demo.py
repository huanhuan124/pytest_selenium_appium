from 普通功能.baseclass_demo import Baseclass_demo


class DogClass(Baseclass_demo):
    print("This is a class")
    address = 'Beijing'  # address就是一个类变量（ class里def外，通过变量名能被赋值）

    def __init__(self, name, age):
        self.name = name  ##类的设计时；def里通过self点运算变量名能被赋值
        print(f"init  {self.name}")
        self.age = age
        print(f"init  {self.age}")
        #self代表类的实例，而非类哪个对象调用方法，那么该方法中的self就代表那个对象==》<class '__main__.DogClass'>
        print(self.__class__)


    def disp_dog_info(self):
        # 使用class_name.attr_name的方式引用类变量
        print(f"disp_dog_info  {self.name}")
        print(f"disp_dog_info  {self.age}")
        print(f"disp_dog_info  {DogClass.address}")

        print('My dog\'s name is {}, {} yesrs old, come from {}.'.format(self.name, self.age,
                                                                         DogClass.address))
        print(self.__class__)
        setattr(self.__class__,"mem","test")


    def mod_dog_info(self, age_new, addr_new):
        self.age = age_new
        DogClass.address = addr_new  # def里通过类对象即类名字的点运算变量名可被赋值
        print(f"mod_dog_info  {self.name}")
        print(f"mod_dog_info  { self.age}")
        print(f"mod_dog_info  {DogClass.address}")


print("")
my_dog1 = DogClass('WangWang', 4)  # 实例化
my_dog2 = DogClass('PangPang', 3)  # 实例化
# my_dog1.disp_dog_info()  #
# my_dog2.disp_dog_info()
#
# print("")
# my_dog1.mod_dog_info(1, 'Shanghai')
# my_dog1.disp_dog_info()
# my_dog2.disp_dog_info()
#
# print("")
# DogClass.address = 'ShenZhen'  ##程序里：通过类对象(类名字)的点运算类名字也可被赋值
# my_dog1.disp_dog_info()
# my_dog2.disp_dog_info()

print("")
my_dog2.name = 'HuaHua'  # 程序里；通过实例对象的点运算变量名可被赋值
my_dog2.disp_dog_info()
