# -*-coding:UTF-8 -*-
from time import sleep
from pymysql import connect
from selenium import webdriver
from selenium.webdriver.support.select import Select

class TestGoods():
    def login(self):
        driver = webdriver.Chrome()
        driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
        driver.maximize_window()
        driver.find_element_by_name('username').send_keys('caichang')
        driver.find_element_by_name('password').send_keys('caichang1')
        driver.find_element_by_class_name('btn-a').click()    
        return driver
    
    def get_connect(self):
        cn = connect('192.168.1.4', 'root', 'root', 'ecshop', 3306)
        return cn
    
    def get_cursor(self):
        cursor=self.get_connect().cursor()
        return cursor
    
    def closeall(self):
        self.get_connect().close()
        self.get_cursor().close()
    
    def test_add(self):
            
        self.get_cursor().execute("delete from ecs_goods where goods_name='iphone'")
        self.get_connect().commit()
        driver=self.login()
        driver.switch_to.frame('menu-frame')
        driver.find_element_by_link_text('添加新商品').click()
        driver.switch_to.default_content()
        driver.switch_to.frame('main-frame')
        driver.find_element_by_name('goods_name').send_keys('iphone')
        Select(driver.find_element_by_name('cat_id')).select_by_visible_text('    小型手机')
        driver.find_element_by_xpath('//*[@id="tabbody-div"]/form/div/input[2]').click()
         
        sleep(2)
        
        cursor=self.get_cursor()
        cursor.execute("select goods_name from ecs_goods where goods_name='iphone'")
        result = self.get_cursor().fetchone()
        
        
        assert result[0] == 'iphone'
#         if result[0] == 'iphone':
#             print('添加新商品成功')
#         else:
#             print('添加商品失败')
        
        self.closeall()
        driver.close()


