# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utils.Config import Config
from utils.Logger import Logger

logger = Logger('Browser').getlog()


class Browser(object):
    '''
            鼠标事件只封装了一个
            键盘事件没必要封装
            下拉框也只封装一个最最常用的行为
    '''
    dir = os.path.dirname(os.path.abspath('.'))
    
    chrome_driver_path = dir + '\\config2\\devicedriver\\chromedriver.exe'
    firefox_driver_path = dir + '\\devicedriver\\'
    ie_driver_path = dir + '\\devicedriver\\'
    
    def __init__(self):
        self.driver = None
        
    def open_browser(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '\\config2\\conf\\config.ini'
        # 加载自己的配置文件类
        config = Config(file_path)
        browser = config.get_value(file_path, "Browser", "browserName")
        url = config.get_value(file_path, "Server", "url")
    
        if browser == "Firefox":
            self.driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info('打开了Firefox浏览器')
        elif browser == "Chrome":
            self.driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info('打开了Chrome浏览器')
        elif browser == "IE":
            self.driver = webdriver.Ie(self.ie_driver_path)
            logger.info('打开了IE浏览器')
        else:
            logger.info("找不到 %s 浏览器,你应该从这里面选取一个 'Firefox', 'Chrome', 'IE'" % self.driver)
            raise NameError("找不到 %s 浏览器,你应该从这里面选取一个 'Firefox', 'Chrome', 'IE'" % self.driver)
        
        self.driver.get(url)
        logger.info('浏览器地址为：' + url)
        self.driver.maximize_window()
        logger.info('最大化浏览器')
        return self.driver

    def waitElemnet(self, selector_by, selector_value, secs=5):
        try:
            # 实在写不下去所有了，自己扩展出所有，一般感觉有这些够了
            if selector_by == "id":
                WebDriverWait(self.driver, secs, 1).until(expected_conditions.presence_of_element_located((By.ID, selector_value)))
            elif selector_by == "name":
                WebDriverWait(self.driver, secs, 1).until(expected_conditions.presence_of_element_located((By.NAME, selector_value)))
            elif selector_by == "link_text":
                WebDriverWait(self.driver, secs, 1).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, selector_value)))
            elif selector_by == "partial_link_text":
                WebDriverWait(self.driver, secs, 1).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)))
            elif selector_by == "xpath":
                WebDriverWait(self.driver, secs, 1).until(expected_conditions.presence_of_element_located((By.XPATH, selector_value)))
            elif selector_by == "class_name":
                WebDriverWait(self.driver, secs, 1).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, selector_value)))             
            elif selector_by == "css_selector":
                WebDriverWait(self.driver, secs, 1).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, selector_value)))
            else:
                logger.info("语法错误，参考: 'id=>caichang 或 xpath=>//*[@id='caichang'].")
                raise NoSuchElementException("语法错误，参考: 'id=>caichang 或 xpath=>//*[@id='caichang'].")
        except (TimeoutException, NoSuchElementException):
            logger.error("查找元素超时，请检查元素")

    def find_element(self, selector):
        # 根据=>来切割字符串，submit_btn = "id=>caichang"
        
        element = ''
        
        if '=>' not in selector:
            logger.info('对不起，至少要包含=>符')
            raise Exception('对不起，至少要包含=>符')
        
        # 如果包含了=>字符传后开始切割
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        # 查找元素，超时抛异常
        self.waitElemnet(selector_by, selector_value)

        # 实在写不下去所有了，自己扩展出所有，一般感觉有这些够了
        if selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif  selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)            
        elif selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            element = self.driver.find_element_by_css_selector(selector_value)
        
        return element

    def input(self, selector, text):
    # 输入内容
        self.find_element(selector).send_keys(text)
        logger.info('往元素' + selector + '输入了值：' + text)
    
    def click(self, selector):
        self.find_element(selector).click()
        logger.info('点击了' + selector)

    def switch(self):
        switch = self.driver.switch_to
        return switch
    
    def into_frame(self, frame_name):
        self.switch().frame(frame_name)
        
    def default_content(self):
        self.switch().default_content()
    
    # 根据下拉框的文本来选择内容
    def select_by_text(self, selector, text):
        try:
            Select(self.find_element(selector)).select_by_visible_text(text)
            logger.info('往元素' + selector + '选择了值：' + text)
        except Exception:
            logger.info('找不到下拉框的值，请确认')

    # 获得弹出框文本
    def alert_text(self):
        logger.info('弹出框文本为：' + self.driver.switch_to.alert.text)
        return self.driver.switch_to.alert.text

    # 点击弹出框确定
    def alert_accept(self):
        logger.info('点击了确定按钮')
        self.driver.switch_to.alert.accept()

    # 点击弹出框取消
    def alert_cancel(self):
        logger.info('点击了取消按钮')
        self.driver.switch_to.alert.dismiss()

    # 移动到某元素，点击一下
    def move_and_click(self, element):
        logger.info('移动到元素上点击了一下元素')
        ActionChains(self.driver).move_to_element(self.find_element(element)).perform()

    # 移动到某元素，点击一下
    def move_and_click2(self, element):
        logger.info('移动到元素上点击了一下元素')
        ActionChains(self.driver).move_to_element(self.find_element(element)).click()
    
    
    def back(self):
        logger.info('回退了一步')
        self.driver.back()
    
    def forward(self):
        logger.info('跳转了浏览器')
        self.driver.forward()

    def refresh(self):
        logger.info('刷新了浏览器')
        self.driver.refresh()
    
    # 获取元素属性值
    def get_attr(self, selector, attr_name):
        logger.info('name可以是textContent，value或自身元素的属性：' + self.find_element(selector).get_attribute(attr_name))
        return self.find_element(selector).get_attribute(attr_name)
    
    def close(self):
        logger.info('关闭了浏览器')
        self.driver.close()
        
