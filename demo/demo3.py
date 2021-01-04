# -*- coding: utf-8 -*-
from json import loads

from requests.api import get, post

from utils.Logger import Logger

logger = Logger('TestEducation').getlog()


class TestEducation():

    def tes_login(self):
        url = 'http://192.168.1.5:8080/recruit.students/login/in'
        params = {
            'account':'admin',
            'pwd':'660B8D2D5359FF6F94F8D3345698F88C'
        }
        cookies = {
            'JSESSIONID':'4C7F9900296CCF401EA453523988978F'
        }
        logger.info('url为：' + url)
        response = get(url, params, cookies=cookies)
        logger.info('我的状态码为%s' % response.status_code)
        # print(response)
        # print(response.text)
        # print(response.status_code)
        assert response.status_code == 200

    def tes_addSchool(self):
        url = 'http://192.168.1.5:8080/recruit.students/school/manage/addSchoolInfo'
        data = {
            'schoolName':'蔡包子4',
            'listSchoolType[0].id':'2',
            'canRecruit':'1',
            'remark':'3333'
        }
        cookies = {
            'JSESSIONID':'4C7F9900296CCF401EA453523988978F'
        }
        logger.info('url为：' + url)
        response = post(url, data, cookies=cookies)
        logger.info('我的状态码为%s:' % response.status_code)
        logger.info('返回内容为%s:' % loads(response.text))
        # print(response)
        # print(response.text)
        # print(response.status_code)
        print(response.text)
        assert response.status_code == 200 and loads(response.text)['code'] == 1
    
    def test_setRecruitTime(self):
        url = 'http://192.168.1.5:8080/recruit.students/school/manage/setStudentRecruitTime'
        json = [{"id":"4601", "recruitStartTime":"2021-01-04", "recruitEndTime":"2021-01-12", "isStudentRecruitTime":"1"}]
        
        cookies = {
            'JSESSIONID':'4C7F9900296CCF401EA453523988978F'
        }
        
        headers = {
            'Content-Type':'application/json'
        }
        
        logger.info('url为：' + url)
        response = post(url, json=json, cookies=cookies, headers=headers)
        logger.info('我的状态码为%s:' % response.status_code)
        logger.info('返回内容为%s:' % loads(response.text))
        # print(response)
        # print(response.text)
        # print(response.status_code)
        print(response.text)
        assert response.status_code == 200 and loads(response.text)['code'] == 1
    
