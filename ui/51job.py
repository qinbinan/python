# -*-coding:UTF-8 -*-
from selenium import webdriver
from time import sleep
from xlutils.copy import copy
from xlrd import open_workbook



driver = webdriver.Chrome()
driver.get('https://login.51job.com/login.php')
driver.maximize_window()
driver.find_element_by_id('loginname').send_keys('15920413866')
driver.find_element_by_id('password').send_keys('xiu360360')
driver.find_element_by_id('login_btn').click()
driver.find_element_by_link_text('职位搜索').click()
driver.find_element_by_id('keywordInput').send_keys('软件测试工程师')
driver.find_element_by_id('search_btn').click()
sleep(2)
driver.find_element_by_class_name('chall').click()
# company_list = []
# for i in range(1, 51):
#     company = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[%d]/div[2]/a' % i).text
#     company_list.append(company)
# orig_xls = open_workbook(r'd:\emp.xls', formatting_info=True)
# new_xls = copy(orig_xls)
# sheet = new_xls.get_sheet(2)
# sheet.write(0, 0, '公司信息')
# for i in range(len(company_list)):
#     sheet.write(i+1,0,company_list[i])


bk=open_workbook(r'd:\emp.xls')
sheet=bk.sheet_by_name('黑名单公司')
black_list=sheet.col_values(0,1)
for i in range(len(black_list)):
    driver.find_element_by_xpath("//div[@class='er']//a[@title='%s']//../preceding-sibling::div[1]"  % black_list[i]).click()

driver.close()
    
    




