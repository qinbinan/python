# -*-coding:UTF-8 -*-
from pymysql import connect
from selenium import webdriver
from time import sleep

cn = connect('192.168.1.4', 'root', 'root', 'ecshop', 3306)
cursor = cn.cursor()
cursor.execute("select is_on_sale from ecs_goods where goods_name='iphone'")
result=cursor.fetchone()
 
driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin')
driver.maximize_window()
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_xpath('//*[@id="loginPanel"]/div[3]/input').click()
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')
driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[13]/td[5]/img').click()
sleep(2)
cursor.execute("select is_on_sale from ecs_goods where goods_name='iphone'")
result2=cursor.fetchone()

if result[0]!=result2[0] and result2[0]==0:
    print('下架成功')
else:
    print('上架成功')



# from selenium import webdriver
# 
# driver = webdriver.Chrome('../drivers/chromedriver.exe')
# driver.get('https://kehu51.com/')
# driver.maximize_window()
# driver.find_element_by_id('username').send_keys('18601663355')
# driver.find_element_by_id('password').send_keys('Qbn19940402')
# driver.find_element_by_class_name('btn').click()

