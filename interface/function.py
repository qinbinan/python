# -*-coding:UTF-8 -*-
from json import loads
import os
from requests.api import get, post
from utils.Config import Config


class TestEdc():
     
    file_path = os.path.dirname(os.path.abspath('.')) + '\\demo\\conf\\config.ini'
    config = Config(file_path)
    
    '''
            配置cookie文件
    '''
    cookie_id = config.getall_option(file_path, 'Cookies')[0].upper()
    cookie_value = config.get_value(file_path, 'Cookies', 'JSESSIONID')
    
    '''
            配置IP地址以及端口
    '''
    ip = config.getall_option(file_path, 'Env')[0]
    ip_value = config.get_value(file_path, 'Env', 'ip')
    port = config.getall_option(file_path, 'Env')[1]
    port_value = config.get_value(file_path, 'Env', 'port')
    
    '''
            配置申请头
    '''
    content_type=config.getall_option(file_path,'Headers')[0]
    content_type_value=config.get_value(file_path,'Headers','Content-Type')
       
    cookies = {
            cookie_id:cookie_value
            }
    env = {
        ip:ip_value,
        port:port_value
        }
    headers = {
        content_type:content_type_value
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
            'schoolName':'实验中学3',
            'listSchoolType[0].id':'3',
            'canRecruit':'1',
            'remark':'chong'
           }
        response = post(url, data=data, cookies=self.cookies)
        self.config.create_section(self.file_path,'DynamicId')
        self.config.create_value(self.file_path,'DynamicId','f_id','%s' % loads(response.text)['data']['id'] )
        self.config.create_value(self.file_path,'DynamicId','l_id','%s' % loads(response.text)['data']['laccount'] )
        assert response.status_code == 200 and (loads(response.text))['code'] == 1

                    
    '''
             功能：设置学生录入时间
         
    '''
  
    def test_ssr(self):
        f_id=self.config.get_value(self.file_path,'DynamicId','f_id')
        url = '%s:%s/recruit.students/school/manage/setStudentRecruitTime' % (self.env['ip'], self.env['port'])
        json = [{"id":f_id, "recruitStartTime":"2021-01-05", "recruitEndTime":"2021-01-07", "isStudentRecruitTime":"1"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
         
    '''
             功能：设置招生录取时间
         
    '''
  
    def test_set(self):
        f_id=self.config.get_value(self.file_path,'DynamicId','f_id')
        url = '%s:%s/recruit.students/school/manage/setEnrollmentTime' % (self.env['ip'], self.env['port'])
        json = [{"id":f_id, "startTime":"2020-12-28", "endTime":"2020-12-31", "isSelfEnrollmentTime":"1"}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
         
    '''
             功能：重置密码
         
    '''
  
    def test_rp(self):
        f_id=self.config.get_value(self.file_path,'DynamicId','f_id')
        l_id=self.config.get_value(self.file_path,'DynamicId','l_id')
        url = '%s:%s/recruit.students/school/manage/resetPassword' % (self.env['ip'], self.env['port'])
        json = [{"id":l_id, "schoolId":f_id}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
         
    '''
             功能：启用
         
    '''
  
    def test_es(self):
        f_id=self.config.get_value(self.file_path,'DynamicId','f_id')
        l_id=self.config.get_value(self.file_path,'DynamicId','l_id')
        url = '%s:%s/recruit.students/school/manage/enableOrDisableSchool' % (self.env['ip'], self.env['port'])
        json = [{"id":l_id, "disable":1, "schoolId":f_id}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1
         
    '''
             功能：禁用
         
    '''
  
    def test_ds(self):
        f_id=self.config.get_value(self.file_path,'DynamicId','f_id')
        l_id=self.config.get_value(self.file_path,'DynamicId','l_id')
        url = '%s:%s/recruit.students/school/manage/enableOrDisableSchool' % (self.env['ip'], self.env['port'])
        json = [{"id":l_id, "disable":0, "schoolId":f_id}]
        response = post(url, None, json=json, cookies=self.cookies, headers=self.headers)
        assert response.status_code == 200 and (loads(response.text))['code'] == 1       
