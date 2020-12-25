# -*-coding:UTF-8 -*-
from selenium import webdriver
from time import sleep
from pymysql import connect
from selenium.common.exceptions import NoSuchElementException

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
        conn = connect('192.168.1.4', 'root', 'root', 'ecshop', 3306)
        return conn
    
    def get_cursor(self):
        cursor = self.get_connect().cursor()
        return cursor
    
    def into(self):
        driver = self.login()
        driver.switch_to.frame('menu-frame')
        driver.find_element_by_link_text('商品列表').click()
        driver.switch_to.default_content()
        driver.switch_to.frame('main-frame')
        return driver

    def closeall(self):
        self.get_connect().close()
        self.get_cursor().close()
        
    def test_search(self):
        driver = self.login()
        
        sleep(1)
        driver.switch_to.frame('menu-frame')
        driver.find_element_by_link_text('商品列表').click()
        driver.switch_to.default_content()
        driver.switch_to.frame('main-frame')
        
        sleep(2)
        driver.find_element_by_name('keyword').send_keys('车')
        driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()
        
        sleep(1)
        try:
            search_text = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
            search_total = driver.find_element_by_id('totalRecords').text

            cursor = self.get_cursor()
            cursor.execute("select goods_name from ecs_goods where goods_name like '%车%'")
            
            rs = cursor.fetchall()
            # print(rs)
            
            cursor.execute("select count(*) from ecs_goods where goods_name like '%车%'")
            total = cursor.fetchone()
            assert search_text == rs[0][0] and int(search_total) == total[0]
        except NoSuchElementException:
            print('对不起，没有数据，无法执行删除操作')
        finally:
            self.closeall()
            driver.quit()


