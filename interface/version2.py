# -*-coding:UTF-8 -*-
from json import loads
import os

from requests.api import get, post

from utils.Config import Config


class TestEdc():
    
    file_path = os.path.dirname(os.path.abspath('.')) + '\\conf\\config.ini'
    print(file_path)
    config = Config(file_path)
    '''
            配置cookie文件
    '''
    cookie_id = config.getall_option(file_path, 'Cookies')[0].upper()
    cookie_value = config.get_value(file_path, 'Cookies', 'JSESSIONID')

    ip = config.getall_option(file_path, 'Env')[0]
    ip_value = config.get_value(file_path, 'Env', 'ip')
    port = config.getall_option(file_path, 'Env')[1]
    port_value = config.get_value(file_path, 'Env', 'port')
     
    cookies = {
            cookie_id:cookie_value
            }
    env = {
        ip:ip_value,
        port:port_value
        }
    headers = {
        'Content-Type':'application/json'
        }
    '''
             功能：登录
      
    '''
 
    def test_login(self):
        url = '%s:%s/recruit.students/login/in' % (self.env['ip'], self.env['port'])
        params = {
            'account':'admin',
            'pwd':'660B8D2D5359FF6F94F8D3345698F88C'
        }
        response = get(url, params, cookies=self.cookies)
        assert response.status_code == 200
      
    '''
             功能：新建学校
      
    '''
 
    def est_asi(self):
        url = '%s:%s/recruit.students/school/manage/addSchoolInfo' % (self.env['ip'], self.env['port'])
        data = {
            'schoolName':'实验中学4',
            'listSchoolType[0].id':'3',
            'canRecruit':'1',
            'remark':'chong'
           }
        response = post(url, data=data, cookies=self.cookies)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
        f_id = loads(response.text)['data']['id']
        l_id = loads(response.text)['data']['laccount']
                   
    '''
             功能：设置学生录入时间
        
    '''
 
    def est_ssr(self):
        url = '%s:%s/recruit.students/school/manage/setStudentRecruitTime' % (self.env['ip'], self.env['port'])
        json = [{"id":"4610", "recruitStartTime":"2021-01-05", "recruitEndTime":"2021-01-07", "isStudentRecruitTime":"1"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
        
    '''
             功能：设置招生录取时间
        
    '''
 
    def est_set(self):
        url = '%s:%s/recruit.students/school/manage/setEnrollmentTime' % (self.env['ip'], self.env['port'])
        json = [{"id":"4610", "startTime":"2020-12-28", "endTime":"2020-12-31", "isSelfEnrollmentTime":"1"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
        
    '''
             功能：重置密码
        
    '''
 
    def est_rp(self):
        url = '%s:%s/recruit.students/school/manage/resetPassword' % (self.env['ip'], self.env['port'])
        json = [{"id":"475413", "schoolId":"4610"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
        
    '''
             功能：启用
        
    '''
 
    def est_es(self):
        url = '%s:%s/recruit.students/school/manage/enableOrDisableSchool' % (self.env['ip'], self.env['port'])
        json = [{"id":"475413", "disable":1, "schoolId":"4610"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
        
    '''
             功能：禁用
        
    '''
 
    def est_ds(self):
        url = '%s:%s/recruit.students/school/manage/enableOrDisableSchool' % (self.env['ip'], self.env['port'])
        json = [{"id":"475413", "disable":0, "schoolId":"4610"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1       
