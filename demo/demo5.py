# -*- coding: utf-8 -*-
from json import loads

from requests.api import get, post

from utils.Logger import Logger

import os

from utils.Config import Config

logger = Logger('TestEducation').getlog()


class TestEducation():
    
    file_path = os.path.dirname(os.path.abspath('.')) + '\\interface\\conf\\config.ini'
    config = Config(file_path)
    
    #cookie配置文件属性
    jsessionid = config.getall_option(file_path,'Cookies')[0].upper()
    cookie_value = config.get_value(file_path, "Cookies", "JSESSIONID")
    
    #env配置文件属性
    ip = config.getall_option(file_path,'Env')[0]
    ip_value = config.get_value(file_path, "Env", "ip")   
    port = config.getall_option(file_path,'Env')[1]
    port_value = config.get_value(file_path, "Env", "port")     
    
    #header配置文件属性
    content_type = config.getall_option(file_path,'Headers')[0]
    content_type_value = config.get_value(file_path, "Headers", "Content-Type")
    
    
    cookies = {
        jsessionid:cookie_value
    }
    
    env = {
        ip:ip_value,
        port:port_value
    }
    
    
    headers = {
        content_type:content_type_value
    }

    def tes_login(self):
        url = 'http://%s:%s/recruit.students/login/in' % (self.env['ip'], self.env['port'])
        params = {
            'account':'admin',
            'pwd':'660B8D2D5359FF6F94F8D3345698F88C'
        }
        
        logger.info('url为：' + url)
        response = get(url, params, cookies=self.cookies)
        logger.info('我的状态码为%s' % response.status_code)
        assert response.status_code == 200

    def test_addSchool(self):
        url = 'http://192.168.1.5:8080/recruit.students/school/manage/addSchoolInfo'
        data = {
            'schoolName':'蔡包子40',
            'listSchoolType[0].id':'2',
            'canRecruit':'1',
            'remark':'3333'
        }
        logger.info('url为：' + url)
        response = post(url, data, cookies=self.cookies)
        #print(response.text)
        logger.info('我的状态码为%s:' % response.status_code)
        logger.info('返回内容为%s:' % loads(response.text))
        
        logger.info(loads(response.text)['data']['id'])
        logger.info(type(loads(response.text)['data']['id']))
        #return loads(response.text)['data']['id']
        self.config.create_section(self.file_path, 'DynamicId')
        self.config.create_value(self.file_path, 'DynamicId','id',"%s" %loads(response.text)['data']['id'])
        
        assert response.status_code == 200 and loads(response.text)['code'] == 1
       
    
    '''
            功能：设置学生录入时间
            作者：蔡昶
            创建时间：2021-01-4
            版本；1.0
    '''
    def test_setRecruitTime(self):
        dynamic_id = self.config.get_value(self.file_path, "DynamicId", "id")

        url = 'http://192.168.1.5:8080/recruit.students/school/manage/setStudentRecruitTime'
        json = [{"id":dynamic_id, "recruitStartTime":"2021-01-04", "recruitEndTime":"2021-01-12", "isStudentRecruitTime":"1"}]
        logger.info('url为：' + url)
        response = post(url, json=json, cookies=self.cookies, headers=self.headers)
        logger.info('我的状态码为%s:' % response.status_code)
        logger.info('返回内容为%s:' % loads(response.text))
        print(response.text)
        assert response.status_code == 200 and loads(response.text)['code'] == 1
    
