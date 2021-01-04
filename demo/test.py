# -*- coding: utf-8 -*-
# from json import loads
# 
# from requests.api import post
# 
# 
# url = 'http://192.168.1.5:8080/recruit.students/school/manage/addSchoolInfo'
# data = {
#     'schoolName':'蔡包子2',
#     'listSchoolType[0].id':'2',
#     'canRecruit':'1',
#     'remark':'3333'
# }
# cookies = {
#     'JSESSIONID':'4C7F9900296CCF401EA453523988978F'
# }
# response = post(url, data, cookies=cookies)
# # print(response)
# # print(response.text)
# # print(response.status_code)
# print(response.text)
# print(type(response.text))
# 
# print(type(loads(response.text)))
# if loads(response.text)['code']==1:
#     print()
import os

from utils.Config import Config


file_path = os.path.dirname(os.path.abspath('.')) + '\\conf\\config.ini'
config = Config(file_path)
browser = config.get_value(file_path, "Browser", "browserName")
print(browser)

print(config.getall_option(file_path,'Cookies'))