# -*- coding: utf-8 -*-
#列表和元组前面的操作全部一样
#创建
empinfo=[]
empinfo=['蜀国','吴国','魏国']
empinfo=[['关羽','张飞','赵云'],['太史慈','甘宁','吕蒙'],['夏侯惇','许褚','张辽']]
#访问和遍历一模一样，这里不写了
for i in range(len(empinfo)):
    for j in range(len(empinfo[i])):
        print(empinfo[i][j])
        
# 列表是数据结构中的链表的知识,因为这个结构，他有自己的独有方法,我们就重点学习这些独有方法
empinfo=['蜀国','吴国','魏国']
empinfo.append('群雄')
print(empinfo)
empinfo.insert(2, (1,'凤姐','选美冠军'))
print(empinfo)


empinfo.pop()
print(empinfo)
empinfo.pop(2)
print(empinfo)
empinfo.remove('魏国')
print(empinfo)

empinfo.clear()
print(empinfo)

