# -*-coding:UTF-8 -*-
from json import loads
from requests.api import get, post
from utils.Logger import Logger

logger = Logger('TestEdc').getlog()


class TestEdc:
    cookies = {
            'JSESSIONID':'53F7CEDF986BC9223EAFD91348A400BA'
            }
    env = {
        'ip':'http://192.168.1.5',
        'port':'8080'
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
    def test_asi(self):
        url = '%s:%s/recruit.students/school/manage/addSchoolInfo' % (self.env['ip'], self.env['port'])
        data = {
            'schoolName':'实验中学',
            'listSchoolType[0].id':'3',
            'canRecruit':'1',
            'remark':'chong'
           }
        response = post(url, data=data, cookies=self.cookies)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
    
    
    '''
         功能：设置学生录入时间
    
    '''
    def test_ssr(self):
        url = '%s:%s/recruit.students/school/manage/setStudentRecruitTime' % (self.env['ip'], self.env['port'])
        json = [{"id":"4610", "recruitStartTime":"2021-01-05", "recruitEndTime":"2021-01-07", "isStudentRecruitTime":"1"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
    
    
    '''
         功能：设置招生录取时间
    
    '''
    def test_set(self):
        url = '%s:%s/recruit.students/school/manage/setEnrollmentTime' % (self.env['ip'], self.env['port'])
        json = [{"id":"4610", "startTime":"2020-12-28", "endTime":"2020-12-31", "isSelfEnrollmentTime":"1"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
    
    
    '''
         功能：重置密码
    
    '''
    def test_rp(self):
        url = '%s:%s/recruit.students/school/manage/resetPassword' % (self.env['ip'], self.env['port'])
        json = [{"id":"475413", "schoolId":"4610"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
    
    
    '''
         功能：启用
    
    '''
    def test_es(self):
        url = '%s:%s/recruit.students/school/manage/enableOrDisableSchool' % (self.env['ip'], self.env['port'])
        json = [{"id":"475413", "disable":1, "schoolId":"4610"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
    
    
    '''
         功能：禁用
    
    '''
    def test_ds(self):
        url = '%s:%s/recruit.students/school/manage/enableOrDisableSchool' % (self.env['ip'], self.env['port'])
        json = [{"id":"475413", "disable":0, "schoolId":"4610"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1       
