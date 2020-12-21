# -*- coding: utf-8 -*-


# 定义
class HomeWork():

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
hw = HomeWork()  #你主观的感觉是用了一个变量去接收这个类，但现在换词了
                 #这个hw叫对象,这个动作成为类的实例化
                 #你想用类里面的任何东西，现在都转给了这个对象，只能对象.出来
ylist = hw.is_leap_year(1, 101, 20)
print(ylist)
