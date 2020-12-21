# -*- coding: utf-8 -*-
# 定义
class HomeWork():
    def __init__(self, sex):
        self.name = ''  # 你不能直接self.name就完事，得有一个初始值
        self.age = 0    
        self.sex = sex
    
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
print(hw.name)
print(hw.age)
ylist =hw.is_leap_year(2020, 3000, 10)
print(ylist)


# 我打开一个文件或我找到某个类，我想玩他，首先进行类的实例化

# 立刻看这个类有没有__init__（初始化）方法，如果有，立刻看有没有参数，如果有，立刻传参

# 这个__init__中的所有定义都是这个类的属性
# 你可以随便的对象.属性或对象.方法来操作这个类

