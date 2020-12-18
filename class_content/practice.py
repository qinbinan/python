# -*-coding:UTF-8 -*-
# 求1-100的

# summ = 0
# for i in range(101):
#     summ += i
# print(summ)
# 
# 
# num_list=[]
# for i in range(101):
#     if i % 3 == 0 and i % 5 != 0:
#         num_list.append(i)
# print(num_list)

def yolo():
    num_list = []
    for i in range(101):
        if i % 3 == 0 and i % 5 != 0:
            num_list.append(i)
    print("100以内能被3整除但是不能被5整除的数:%s" % num_list)

