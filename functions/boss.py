# -*- coding: utf-8 -*-
from selenium import webdriver


driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
name = driver.find_element_by_id('kw')
name.send_keys('caichang')