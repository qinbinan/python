# -*- coding: utf-8 -*-

#_ __：我还是小白的时候，自己写根本不用，但我能看得懂，等你代码有点基础后，就可以玩这2个了
# 定义
class HomeWork():
    
    def __init__(self, sex):
        self.name = ''  # 你不能直接self.name就完事，得有一个初始值
        self.age = 0    #硬赋
        self.sex = sex
        self._weight=0 # 提醒用户我这个有特别用法，别轻易的在外边直接对象调
        self.__friend=['刘德华','凤姐'] #私有化的属性
    
    def _chi(self):
        if self._weight<80:
            print('太胖了')
        self.__he() #一个方法调另外的方法都要带self
        print('好好吃')
    
    def __he(self):
        print('喝得好爽')
    
    def is_leap_year(self, start, end, future):
        total = 0
        year_list = []
        for i in range(start, end):
            if i % 4 == 0:
                year_list.append(i)
                total = total + 1
                if total == future:
                    break
        return year_list


# 调用
#hw = HomeWork()
hw=HomeWork('女')
hw.name = '王苇'
hw.age = 20
print(hw.sex)
print(hw.age)
ylist = hw.is_leap_year(1, 101, 2)
print(ylist)
hw._weight=79
print(hw._weight)
hw._chi()
#print(hw.__friend)
#hw.__he()


# 我打开一个文件或我找到某个类，我想玩他，首先进行类的实例化
caichang=HomeWork(0)
# 立刻看这个类有没有__init__（初始化）方法，如果有，立刻看有没有参数，如果有，立刻传参
caichang=HomeWork(0)
# 这个__init__中的所有定义都是这个类的属性
# 你可以随便的对象.属性或对象.方法来操作这个类

#open_workbook(filename, logfile, verbosity, use_mmap, file_contents, encoding_override, formatting_info, on_demand, ragged_rows)
