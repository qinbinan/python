# -*-coding:UTF-8 -*-
from selenium import webdriver
from pymysql import connect
from time import sleep

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
driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[12]/a[2]/img').click()
driver.find_element_by_name('shop_price').clear()
driver.find_element_by_name('shop_price').send_keys('3500')
driver.find_element_by_name('market_price').clear()
driver.find_element_by_name('market_price').send_keys('4000')
driver.find_element_by_xpath('//*[@id="tabbody-div"]/form/div/input[2]').click()

sleep(2)
cn = connect('192.168.1.4', 'root', 'root', 'ecshop', 3306)
cursor = cn.cursor()
cursor.execute("select shop_price from ecs_goods where goods_name='iphone'")
result = cursor.fetchone()
if result[0] == 3500:
    print('编辑成功')
else:
    print('编辑失败')
