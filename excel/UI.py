# -*-coding:UTF-8 -*-
from selenium import webdriver
from time import sleep
from pymysql import connect

driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')
driver.find_element_by_name('keyword').send_keys('车')
driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()
sleep(1)
webname = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text


conne = connect(host='192.168.1.4', user='root', password="root", database='ecshop', port=3306)
cursor = conne.cursor()
cursor.execute("select goods_name from ecs_goods where goods_name like '%车%'")
result = cursor.fetchall()
print(result)










# from selenium import webdriver
# 
# driver = webdriver.Chrome('../drivers/chromedriver.exe')
# driver.get('https://kehu51.com/')
# driver.maximize_window()
# driver.find_element_by_id('username').send_keys('18601663355')
# driver.find_element_by_id('password').send_keys('Qbn19940402')
# driver.find_element_by_class_name('btn').click()

