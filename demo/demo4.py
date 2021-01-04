# -*- coding: utf-8 -*-
from json import loads

from requests.api import get, post

from utils.Logger import Logger

logger = Logger('TestEducation').getlog()


class TestEducation():
    
    cookies = {
        'JSESSIONID':'4C7F9900296CCF401EA453523988978F'
    }
    
    env = {
        'ip':'192.168.1.5',
        'port':8080
    }
    headers = {
        'Content-Type':'application/json'
    }

    def test_login(self):
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
            'schoolName':'蔡包子5',
            'listSchoolType[0].id':'2',
            'canRecruit':'1',
            'remark':'3333'
        }
        logger.info('url为：' + url)
        response = post(url, data, cookies=self.cookies)
        logger.info('我的状态码为%s:' % response.status_code)
        logger.info('返回内容为%s:' % loads(response.text))
        assert response.status_code == 200 and loads(response.text)['code'] == 1
    
    '''
            功能：设置学生录入时间
            作者：蔡昶
            创建时间：2021-01-4
            版本；1.0
    '''
    def tes_setRecruitTime(self):
        url = 'http://192.168.1.5:8080/recruit.students/school/manage/setStudentRecruitTime'
        json = [{"id":"4601", "recruitStartTime":"2021-01-04", "recruitEndTime":"2021-01-12", "isStudentRecruitTime":"1"}]
        logger.info('url为：' + url)
        response = post(url, json=json, cookies=self.cookies, headers=self.headers)
        logger.info('我的状态码为%s:' % response.status_code)
        logger.info('返回内容为%s:' % loads(response.text))
        print(response.text)
        assert response.status_code == 200 and loads(response.text)['code'] == 1
    
