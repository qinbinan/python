# -*- coding: utf-8 -*-

# 继承
# 1、什么叫继承
# 2、为什么要继承？相同代码写一次
# 3、属性不需要写覆盖关系，直接继承后就拥有；方法可覆写（override），覆写的前提是要和父类的方法名一致，也可直接继承用

#静态属性和静态方法当我不是高手时，不用

class Animal():

    def __init__(self):
        self.eye = ''
        self.ear = ''

    def chi(self):
        print('动物吃')
    
    def pao(self):
        print('动物跑')


class Cat(Animal):
    # ming这个属性并没有写在初始化方法中，也没有带self
    # 这种不在初始化里面定义的属性叫：静态属性
    # 静态属性直接可以被类调用，不走对象
    # 理解成军队的：直属队
    ming = 9 

    def __init__(self):
        self.weiba = ''

    def zhua(self):
        print('抓老鼠')
        
    # 这个chi覆盖了父类的chi
    def chi(self):
        print('猫咪的吃')
      
    #静态方法，他不需要self，在原来的方法基础上加@staticmethod 即可
    @staticmethod
    def pa():
        print('猫咪爬')


class Bird(Animal):

    def fei(self):
        print('我飞飞飞')


class Dog(Cat, Bird):

    # 这个chi覆盖了父类的chi
    def chi(self):
        print('我是用啃的')


tom = Cat()
tom.pao()
tom.chi()
tom.weiba = '翘'
tom.zhua()

# 调ming有2种
print(tom.ming)
print(Cat.ming)  #
Cat.pa()

erha = Dog()
erha.ear = '尖尖的'
erha.eye = '蓝色'
erha.chi()
erha.zhua()
erha.fei()

# driver=webdriver.Chrome()
# driver.ex

