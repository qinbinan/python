# -*-coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
#driver.find_element_by_class_name('btn-a').click()
#键盘的回车事件
driver.find_element_by_class_name('btn-a').send_keys(Keys.ENTER)


driver.switch_to.frame('header-frame')


#driver.find_element_by_link_text('个人设置').click()
#鼠标事件
ActionChains(driver).move_to_element(driver.find_element_by_link_text('个人设置')).perform()

driver.find_element_by_link_text('退出').click()