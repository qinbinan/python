# -*- coding: utf-8 -*-

#写个程序打印出接下来的20个闰年。

def is_leap_year(start,end,future):
    total=0
    year_list=[]
    for i in range(start,end):
        if i%4==0:
            year_list.append(i)
            total=total+1
            if total==future:
                break
    return year_list

year = is_leap_year(100, 500, 30)
print('满足的年份是：%s' %year[:6])

